import os

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QComboBox, QSpinBox, QLineEdit, QPushButton, QFileDialog

from src.helper.common import Globals
from src.widgets.ui_base import BaseUI


class SettingUI(BaseUI):
    def __init__(self):
        self.max_width_index = Globals.config.get(Globals.UserData.max_width_index)
        self.max_width_combo = None
        self.size_spin = None
        self.output_line_edit = None
        super(SettingUI, self).__init__()

    def setup_ui(self):
        super(SettingUI, self).setup_ui()
        max_width_label = QLabel(text="最大宽度", alignment=QtCore.Qt.AlignLeft)
        max_width_combo = QComboBox()
        max_width_combo.addItems(Globals.max_width_arr)
        max_width_combo.setCurrentIndex(self.max_width_index)
        max_width_combo.currentIndexChanged.connect(self.on_combo_changed)

        size_label = QLabel(text="输出字号")
        size_spin = QSpinBox()
        size_spin.setRange(10, 64)
        size_spin.setValue(Globals.config.get(Globals.UserData.font_size))
        size_spin.valueChanged.connect(self.on_save_font_size)

        output_label = QLabel(text="输出目录")
        output_line_edit = QLineEdit(Globals.config.get(Globals.UserData.output_dir))
        output_choose_btn = QPushButton(text="浏览")
        output_choose_btn.clicked.connect(self.on_output_choose_clicked)

        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.addWidget(max_width_label, 0, 0, 1, 1)
        self.main_layout.addWidget(max_width_combo, 0, 1, 1, 1)
        self.main_layout.addWidget(size_label, 1, 0, 1, 1)
        self.main_layout.addWidget(size_spin, 1, 1, 1, 1)
        self.main_layout.addWidget(output_label, 2, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.main_layout.addWidget(output_line_edit, 2, 1, 1, 1)

        self.max_width_combo = max_width_combo
        self.size_spin = size_spin
        self.output_line_edit = output_line_edit

    def on_combo_changed(self):
        self.max_width_index = self.max_width_combo.currentIndex()
        Globals.config.set(Globals.UserData.max_width_index, self.max_width_index)

    def on_save_font_size(self):
        Globals.config.set(Globals.UserData.font_size, self.size_spin.value())

    def on_output_choose_clicked(self):
        where = Globals.config.get(Globals.UserData.custom_dir)
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            Globals.config.set(Globals.UserData.output_dir, dirname)
            self.output_line_edit.setText(dirname)
