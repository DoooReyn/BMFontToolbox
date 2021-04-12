import os

from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QLineEdit,
    QListView,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog,
    QProgressBar
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
        self.image_listview = None
        self.image_list_model = None
        self.start_progress = None
        self.setup_ui()
        self.refresh_images(self.app.config.get("images"))

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(main_layout)

        image_widget = QWidget()
        image_layout = QHBoxLayout()
        image_widget.setLayout(image_layout)

        image_label = QLabel(text='图集目录', alignment=QtCore.Qt.AlignCenter)
        image_line_edit = QLineEdit(self.app.config.get("images"))
        image_choose_btn = QPushButton(text='选择')
        image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        image_layout.addWidget(image_label)
        image_layout.addWidget(image_line_edit)
        image_layout.addWidget(image_choose_btn)

        output_widget = QWidget()
        output_layout = QHBoxLayout()
        output_widget.setLayout(output_layout)

        output_label = QLabel(text='输出目录', alignment=QtCore.Qt.AlignCenter)
        output_line_edit = QLineEdit(self.app.config.get("output"))
        output_choose_btn = QPushButton(text='选择')
        output_choose_btn.clicked.connect(self.on_output_choose_clicked)
        output_layout.addWidget(output_label)
        output_layout.addWidget(output_line_edit)
        output_layout.addWidget(output_choose_btn)

        image_listview = QListView()
        image_list_model = QStandardItemModel(image_listview)
        image_listview.setModel(image_list_model)

        start_widget = QWidget()
        start_layout = QHBoxLayout()
        start_btn = QPushButton(text="执行")
        start_btn.clicked.connect(self.on_start_clicked)
        start_btn.setShortcut("F5")
        start_progress = QProgressBar()
        start_progress.setValue(0)
        start_layout.addWidget(start_progress)
        start_layout.addWidget(start_btn)
        start_widget.setLayout(start_layout)

        main_layout.addWidget(image_widget)
        main_layout.addWidget(output_widget)
        main_layout.addWidget(image_listview)
        main_layout.addWidget(start_widget)

        self.image_line_edit = image_line_edit
        self.output_line_edit = output_line_edit
        self.image_listview = image_listview
        self.image_list_model = image_list_model
        self.start_progress = start_progress

    def refresh_images(self, dirname):
        self.image_list_model.clear()
        self.image_atlas.clear()
        for path in get_image_files(dirname):
            self.image_list_model.appendRow(QStandardItem(path))
            self.image_atlas.append(os.path.join(dirname, path))

    def on_image_choose_clicked(self):
        where = self.app.config.get("images")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.app.config.set("images", dirname)
            self.image_line_edit.setText(dirname)
            self.refresh_images(dirname)

    def on_output_choose_clicked(self):
        where = self.app.config.get("output")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.app.config.set("output", dirname)
            self.output_line_edit.setText(dirname)

    def on_start_clicked(self):
        from_dir = self.image_line_edit.text()
        if not (os.path.exists(from_dir) and os.path.isdir(from_dir)):
            Message.show_error("无效的图集目录！", self)
            return

        output_dir = self.output_line_edit.text()
        if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
            Message.show_error("无效的输出目录！", self)
            return

        if len(self.image_atlas) <= 0:
            Message.show_error("图集目录下未找到有效图集！", self)
            return

        FontFactory.run_with(FontMode.Atlas, {
            "from": self.image_line_edit.text(),
            "output": self.output_line_edit.text(),
            "atlas": self.image_atlas
        })
