import os

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QComboBox, QSpinBox, QLineEdit, QFileDialog, QRadioButton, \
    QButtonGroup

from helper.common import Globals
from widgets.ui_base import BaseUI


class SettingUI(BaseUI):
    def __init__(self):
        self.max_width_index = Globals.config.get(Globals.UserData.max_width_index)
        self.max_width_combo = None
        self.size_spin = None
        self.output_name_edit = None
        self.output_line_edit = None
        super(SettingUI, self).__init__()

    def setup_ui(self):
        super(SettingUI, self).setup_ui()
        max_width_label = QLabel(text="最大宽度", alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        max_width_combo = QComboBox()
        max_width_combo.addItems(Globals.max_width_arr)
        max_width_combo.setCurrentIndex(self.max_width_index)
        max_width_combo.currentIndexChanged.connect(self.on_combo_changed)

        size_label = QLabel(text="输出字号", alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        size_spin = QSpinBox()
        size_spin.setRange(10, 64)
        size_spin.setValue(Globals.config.get(Globals.UserData.font_size))
        size_spin.valueChanged.connect(self.on_save_font_size)

        output_name_label = QLabel(text="输出名称", alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        output_name_edit = QLineEdit(Globals.config.get(Globals.UserData.font_save_name))
        output_name_edit.textEdited.connect(self.on_output_name_edited)

        output_label = QLabel(text="输出目录", alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        output_line_edit = QLineEdit(Globals.config.get(Globals.UserData.output_dir))
        output_line_edit.setReadOnly(True)
        output_line_edit.cursorPositionChanged.connect(self.on_output_choose_clicked)

        mode_1_radio = QRadioButton("图集模式")
        mode_2_radio = QRadioButton("字体模式")
        mode_1_radio.setChecked(True)
        mode_1_radio.toggled.connect(self.on_mode_1_radio_toggled)
        mode_radio_group = QButtonGroup(self)
        mode_radio_group.addButton(mode_1_radio, 0)
        mode_radio_group.addButton(mode_2_radio, 1)

        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.setColumnStretch(3, 1)
        self.main_layout.addWidget(mode_1_radio, 0, 0, 1, 1)
        self.main_layout.addWidget(mode_2_radio, 0, 1, 1, 1)
        self.main_layout.addWidget(output_name_label, 1, 0, 1, 1)
        self.main_layout.addWidget(output_name_edit, 1, 1, 1, 1)
        self.main_layout.addWidget(max_width_label, 1, 2, 1, 1)
        self.main_layout.addWidget(max_width_combo, 1, 3, 1, 1)
        self.main_layout.addWidget(output_label, 2, 0, 1, 1)
        self.main_layout.addWidget(output_line_edit, 2, 1, 1, 1)
        self.main_layout.addWidget(size_label, 2, 2, 1, 1)
        self.main_layout.addWidget(size_spin, 2, 3, 1, 1)

        self.max_width_combo = max_width_combo
        self.size_spin = size_spin
        self.output_name_edit = output_name_edit
        self.output_line_edit = output_line_edit

    @staticmethod
    def on_mode_1_radio_toggled(state):
        Globals.signal.mode_trigger.emit(state and Globals.Mode.atlas.value or Globals.Mode.font.value)

    def on_combo_changed(self):
        self.max_width_index = self.max_width_combo.currentIndex()
        Globals.config.set(Globals.UserData.max_width_index, self.max_width_index)

    def on_save_font_size(self):
        Globals.config.set(Globals.UserData.font_size, self.size_spin.value())

    def on_output_choose_clicked(self):
        where = Globals.config.get(Globals.UserData.output_dir)
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            Globals.config.set(Globals.UserData.output_dir, dirname)
            self.output_line_edit.setText(dirname)

    def on_output_name_edited(self):
        Globals.config.set(Globals.UserData.font_save_name, self.output_name_edit.text())
