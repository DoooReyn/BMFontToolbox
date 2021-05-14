import os

from PySide6 import QtCore
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QLabel, QComboBox, QRadioButton, QButtonGroup, QPushButton, QPlainTextEdit, QLineEdit, \
    QFileDialog
from getfontname import get_font_name

from src.helper.common import Globals
from src.helper.path import get_system_fonts
from src.toolbox.font import FontFactory, FontMode
from src.widgets.message import Message
from src.widgets.ui_base import BaseUI


class MLineEdit(QPlainTextEdit):
    def __init__(self):
        super(MLineEdit, self).__init__()
        self.timer_id = self.startTimer(100, timerType=QtCore.Qt.VeryCoarseTimer)
        self.current_text = self.toPlainText()

    @staticmethod
    def filter(text):
        text = text.replace("\n", "").replace("\t", "")
        return "".join(sorted(list(set(text))))

    def timerEvent(self, e):
        text = self.toPlainText()
        if self.current_text != text:
            self.current_text = self.filter(text)
            self.setPlainText(self.current_text)


class FontUI(BaseUI):
    def __init__(self):
        self.system_fonts = get_system_fonts()
        self.font_combo = None
        self.input_edit = None
        self.custom_btn = None
        self.custom_edit = None
        self.custom_family = None
        self.custom_font_path = None
        Globals.signal.export_trigger.connect(self.on_export)
        super(FontUI, self).__init__()

    def setup_ui(self):
        super(FontUI, self).setup_ui()

        sys_radio = QRadioButton("系统字体")
        sys_radio.setChecked(True)
        font_combo = QComboBox()
        for item in self.system_fonts:
            font_combo.addItem(item[1])
        font_combo.setCurrentIndex(0)
        font_combo.currentIndexChanged.connect(self.refresh_font)

        custom_radio = QRadioButton("自选字体")
        custom_radio.setCheckable(True)
        custom_radio.setChecked(False)
        custom_radio.toggled.connect(self.on_custom_radio_toggled)
        custom_edit = QLineEdit()
        custom_edit.setPlaceholderText("自定义字体（*.ttf, *.otf）")
        custom_edit.setReadOnly(True)
        custom_edit.setEnabled(False)
        custom_btn = QPushButton(text="浏览")
        custom_btn.setEnabled(False)
        custom_btn.clicked.connect(self.on_custom_clicked)

        font_group = QButtonGroup(self)
        font_group.addButton(sys_radio, 0)
        font_group.addButton(custom_radio, 1)
        font_group.setExclusive(True)

        input_label = QLabel("输出字符")
        input_edit = MLineEdit()
        import_btn = QPushButton(text="从文本文件导入")
        import_btn.clicked.connect(self.on_import_btn_clicked)

        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.addWidget(sys_radio, 1, 0, 1, 1)
        self.main_layout.addWidget(font_combo, 1, 1, 1, 2)
        self.main_layout.addWidget(custom_radio, 2, 0, 1, 1)
        self.main_layout.addWidget(custom_edit, 2, 1, 1, 1)
        self.main_layout.addWidget(custom_btn, 2, 2, 1, 1)

        self.main_layout.addWidget(input_label, 3, 0, 1, 1)
        self.main_layout.addWidget(import_btn, 3, 2, 1, 1)
        self.main_layout.addWidget(input_edit, 4, 0, 1, 3)

        self.input_edit = input_edit
        self.font_combo = font_combo
        self.custom_btn = custom_btn
        self.custom_edit = custom_edit

        self.refresh_font()

    def on_import_btn_clicked(self):
        where = Globals.config.get(Globals.UserData.import_text_dir)
        url, types = QFileDialog().getOpenFileName(dir=where, filter="Text Files Only (*.txt)")
        if url is not None and url != "":
            Globals.config.set(Globals.UserData.import_text_dir, os.path.abspath(os.path.dirname(url)))
            with open(url, "rt", encoding="utf8") as f:
                self.input_edit.setPlainText(f.read())

    def on_custom_radio_toggled(self, state):
        self.custom_btn.setEnabled(state)
        self.custom_edit.setEnabled(state)
        self.font_combo.setEnabled(not state)

    def get_font_path(self):
        if self.font_combo.isEnabled():
            return self.system_fonts[self.font_combo.currentIndex()][0]
        return self.custom_font_path

    def on_export(self):
        if not self.isEnabled() or not self.isVisible():
            return

        output_dir = Globals.config.get(Globals.UserData.output_dir)
        if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
            Message.show_error("无效的输出目录！", self)
            return

        where = self.get_font_path()
        if not where:
            Message.show_error("请选择字体", Globals.main_window)
            return

        chars = self.input_edit.toPlainText()
        if len(chars) <= 0:
            Message.show_error("请填写有效的输出字符", Globals.main_window)
            return

        FontFactory().run_with(FontMode.Ttf, {
            "where": where,
            "output": output_dir,
            "max_width": Globals.get_max_width(),
            "chars": chars,
            "font_size": Globals.config.get(Globals.UserData.font_size)
        })

    def on_filter_input_text(self):
        self.input_edit.setPlainText("".join(set(self.input_edit.toPlainText())))

    def on_custom_clicked(self):
        where = Globals.config.get(Globals.UserData.custom_dir)
        url, types = QFileDialog().getOpenFileName(dir=where, filter="Font Files Only (*.ttf)")
        if url is not None and url != "":
            QFontDatabase.addApplicationFont(url)
            names = get_font_name(url)
            self.custom_font_path = url
            self.custom_family = names[0][0]
            self.custom_edit.setText(self.custom_family)
            Globals.config.set(Globals.UserData.custom_dir, os.path.abspath(os.path.dirname(url)))
            self.refresh_font()
        else:
            self.custom_edit.setText("")
            self.custom_font_path = None
            self.custom_family = None

    def refresh_font(self):
        font = None
        if self.font_combo.isEnabled():
            index = self.font_combo.currentIndex()
            font_info = self.system_fonts[index]
            if font_info:
                font = QFont()
                font.setFamily(font_info[2])
                font.setBold(font_info[3].lower().find("bold") > -1)
        else:
            if self.custom_family:
                font = QFont(self.custom_family)
        if font:
            font.setPointSize(Globals.config.get(Globals.UserData.font_size))
            self.input_edit.setFont(font)
