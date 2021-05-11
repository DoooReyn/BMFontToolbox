import os

from PySide6 import QtCore
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QLabel, QWidget, QGridLayout, QComboBox, QRadioButton, QButtonGroup, QSpinBox, \
    QPushButton, QPlainTextEdit, QLineEdit, QFileDialog
from getfontname import get_font_name

from src.helper.common import Globals
from src.helper.path import get_system_fonts


class MLineEdit(QPlainTextEdit):
    def filter(self):
        text = self.toPlainText().replace("\n", "").replace("\t", "")
        self.setPlainText("".join(sorted(list(set(text)))))

    def paintEvent(self, e):
        super().paintEvent(e)
        self.filter()


class FontUI(QWidget):
    def __init__(self):
        super().__init__()

        self.system_fonts = get_system_fonts()
        self.radio_group = None
        self.size_spin = None
        self.font_combo = None
        self.input_edit = None
        self.custom_btn = None
        self.custom_edit = None
        self.custom_family = None
        self.main_layout = QGridLayout()
        self.main_layout.setHorizontalSpacing(10)
        self.main_layout.setVerticalSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setLayout(self.main_layout)
        self.setup_ui()

    def setup_ui(self):
        atlas_radio = QRadioButton("图集模式")
        font_radio = QRadioButton("字体模式")
        atlas_radio.setChecked(False)
        atlas_radio.setCheckable(True)
        font_radio.setChecked(True)
        font_radio.setCheckable(True)
        radio_group = QButtonGroup(self)
        radio_group.addButton(atlas_radio, 0)
        radio_group.addButton(font_radio, 1)
        radio_group.setExclusive(True)
        radio_group.buttonToggled.connect(self.on_radio_toggled)

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

        size_label = QLabel(text="字体大小")
        size_spin = QSpinBox()
        size_spin.setRange(10, 64)
        size_spin.setValue(Globals.config.get(Globals.UserData.font_size))
        size_spin.valueChanged.connect(self.refresh_font)

        input_label = QLabel("输入字符")
        input_edit = MLineEdit()

        start_btn = QPushButton(text="导出")
        start_btn.clicked.connect(self.on_start_clicked)
        Globals.signal.execute_trigger.connect(self.on_start_clicked)

        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.addWidget(atlas_radio, 0, 0, 1, 1)
        self.main_layout.addWidget(font_radio, 0, 1, 1, 1)
        self.main_layout.addWidget(sys_radio, 1, 0, 1, 1)
        self.main_layout.addWidget(font_combo, 1, 1, 1, 1)
        self.main_layout.addWidget(custom_radio, 2, 0, 1, 1)
        self.main_layout.addWidget(custom_edit, 2, 1, 1, 1)
        self.main_layout.addWidget(custom_btn, 2, 2, 1, 1)

        self.main_layout.addWidget(size_label, 3, 0, 1, 1)
        self.main_layout.addWidget(size_spin, 3, 1, 1, 1)
        self.main_layout.addWidget(input_label, 4, 0, 1, 1)
        self.main_layout.addWidget(input_edit, 5, 0, 1, 3)
        self.main_layout.addWidget(start_btn, 6, 0, 1, 3)

        self.radio_group = radio_group
        self.size_spin = size_spin
        self.input_edit = input_edit
        self.font_combo = font_combo
        self.custom_btn = custom_btn
        self.custom_edit = custom_edit

        self.refresh_font()

    def on_radio_toggled(self, btn: QRadioButton, state):
        if state:
            Globals.signal.mode_trigger.emit(self.radio_group.checkedId())

    def on_custom_radio_toggled(self, state):
        self.custom_btn.setEnabled(state)
        self.custom_edit.setEnabled(state)
        self.font_combo.setEnabled(not state)

    def on_start_clicked(self):
        pass

    def on_filter_input_text(self):
        self.input_edit.setPlainText("".join(set(self.input_edit.toPlainText())))

    def on_custom_clicked(self):
        where = Globals.config.get(Globals.UserData.custom_dir)
        url, types = QFileDialog().getOpenFileName(dir=where, filter="Font Files Only (*.ttf *.otf)")
        if url is not None and url != "":
            QFontDatabase.addApplicationFont(url)
            names = get_font_name(url)
            self.custom_family = names[0][0]
            self.custom_edit.setText(self.custom_family)
            Globals.config.set(Globals.UserData.custom_dir, os.path.abspath(os.path.dirname(url)))
            self.refresh_font()
        else:
            self.custom_edit.setText("")
            self.custom_family = None

    def refresh_font(self):
        if self.font_combo.isEnabled():
            index = self.font_combo.currentIndex()
            font_info = self.system_fonts[index]
            font = QFont()
            font.setFamily(font_info[2])
            font.setBold(font_info[3].lower().find("bold") > -1)
            font.setPointSize(self.size_spin.value())
            self.input_edit.setFont(font)
        else:
            if self.custom_family:
                font = QFont(self.custom_family)
                font.setPointSize(self.size_spin.value())
                self.input_edit.setFont(font)
        Globals.config.set(Globals.UserData.font_size, self.size_spin.value())