import os

from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QLineEdit,
    QListView,
    QPushButton,
    QGridLayout,
    QFileDialog,
    QComboBox
)

from src.helper.path import get_image_files
from src.toolbox.font import (FontFactory, FontMode)
from src.widgets.message import Message


class MainUI(QWidget):
    def __init__(self, app):
        super(MainUI, self).__init__()
        self.app = app
        self.image_atlas = []
        self.image_line_edit = None
        self.output_line_edit = None
        self.max_width_combo = None
        self.image_listview = None
        self.image_list_model = None
        self.start_progress = None
        self.max_length_valid = str(self.app.config.get("max_length"))
        self.setup_ui()
        self.refresh_images()

    def setup_ui(self):
        main_layout = QGridLayout()

        image_label = QLabel(text='图集目录')
        image_line_edit = QLineEdit(self.app.config.get("images"))
        image_choose_btn = QPushButton(text='浏览')
        image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        output_label = QLabel(text='输出目录')
        output_line_edit = QLineEdit(self.app.config.get("output"))
        output_choose_btn = QPushButton(text='浏览')
        output_choose_btn.clicked.connect(self.on_output_choose_clicked)

        max_width_label = QLabel(text="最大宽度", alignment=QtCore.Qt.AlignLeft)
        max_width_combo = QComboBox()
        max_width_combo.addItems(["128", "256", "512", "1024", "2048", "4096"])

        image_listview = QListView()
        image_list_model = QStandardItemModel(image_listview)
        image_list_model.itemChanged.connect(self.on_image_changed)
        image_listview.setModel(image_list_model)

        start_btn = QPushButton(text="执行")
        start_btn.clicked.connect(self.on_start_clicked)

        main_layout.addWidget(image_label, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        main_layout.addWidget(image_line_edit, 0, 1, 1, 1)
        main_layout.addWidget(image_choose_btn, 0, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        main_layout.addWidget(output_label, 1, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        main_layout.addWidget(output_line_edit, 1, 1, 1, 1)
        main_layout.addWidget(output_choose_btn, 1, 2, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        main_layout.addWidget(max_width_label, 2, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        main_layout.addWidget(max_width_combo, 2, 1, 1, 2)
        main_layout.addWidget(image_listview, 3, 0, 1, 3)
        main_layout.addWidget(start_btn, 4, 0, 1, 3)

        main_layout.setHorizontalSpacing(10)
        main_layout.setVerticalSpacing(10)
        main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setLayout(main_layout)

        self.image_line_edit = image_line_edit
        self.output_line_edit = output_line_edit
        self.max_width_combo = max_width_combo
        self.image_listview = image_listview
        self.image_list_model = image_list_model

    def refresh_images(self):
        self.image_list_model.clear()
        self.image_atlas.clear()
        dirname = self.get_image_dir()
        for path in get_image_files(dirname):
            item = QStandardItem(os.path.splitext(path)[0])
            self.image_list_model.appendRow(item)
            self.image_atlas.append(os.path.join(dirname, path))

    def on_image_choose_clicked(self):
        where = self.app.config.get("images")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.app.config.set("images", dirname)
            self.image_line_edit.setText(dirname)
            self.refresh_images()

    def on_image_changed(self, item):
        row = item.index().row()
        old = self.image_atlas[row]
        new = os.path.join(self.get_image_dir(), item.text() + ".png")
        try:
            os.renames(old, new)
            self.image_atlas[row] = new
        except Exception as e:
            Message.show_error(str(e), self)
            item.setText(os.path.splitext(os.path.basename(old))[0])

    def on_output_choose_clicked(self):
        where = self.app.config.get("output")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.app.config.set("output", dirname)
            self.output_line_edit.setText(dirname)

    def get_image_dir(self):
        return self.image_line_edit.text()

    def get_output_dir(self):
        return self.output_line_edit.text()

    def on_start_clicked(self):
        from_dir = self.get_image_dir()
        if not (os.path.exists(from_dir) and os.path.isdir(from_dir)):
            Message.show_error("无效的图集目录！", self)
            return

        output_dir = self.get_output_dir()
        if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
            Message.show_error("无效的输出目录！", self)
            return

        if len(self.image_atlas) <= 0:
            Message.show_error("图集目录下未找到有效图集！", self)
            return

        FontFactory.run_with(FontMode.Atlas, {
            "image": self.image_line_edit.text(),
            "output": self.output_line_edit.text(),
            "atlas": self.image_atlas,
            "max_width": int(self.max_width_combo.currentText())
        })
