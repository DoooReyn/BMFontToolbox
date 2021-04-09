import os

from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListView, \
    QProgressBar, QFileDialog

from src.helper.path import get_image_files


class MainUI(QWidget):
    def __init__(self, app):
        super(MainUI, self).__init__()
        self.app = app

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)

        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        image_label = QLabel(text='图集目录', alignment=QtCore.Qt.AlignCenter)
        self.image_line_edit = QLineEdit(app.config.get("images"))
        self.image_choose_btn = QPushButton(text='选择')
        self.image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        self.image_layout.addWidget(image_label)
        self.image_layout.addWidget(self.image_line_edit)
        self.image_layout.addWidget(self.image_choose_btn)
        self.image_widget.setLayout(self.image_layout)

        self.output_widget = QWidget()
        self.output_layout = QHBoxLayout()
        output_label = QLabel(text='输出目录', alignment=QtCore.Qt.AlignCenter)
        self.output_line_edit = QLineEdit(app.config.get("output"))
        self.output_choose_btn = QPushButton(text='选择')
        self.output_choose_btn.clicked.connect(self.on_output_choose_clicked)
        self.output_layout.addWidget(output_label)
        self.output_layout.addWidget(self.output_line_edit)
        self.output_layout.addWidget(self.output_choose_btn)
        self.output_widget.setLayout(self.output_layout)

        self.image_listview = QListView()
        self.image_list_model = QStandardItemModel(self.image_listview)
        for path in get_image_files(app.config.get("images")):
            self.image_list_model.appendRow(QStandardItem(path))
        self.image_listview.setModel(self.image_list_model)

        self.start_widget = QWidget()
        self.start_layout = QHBoxLayout()
        self.start_btn = QPushButton(text="执行")
        self.start_btn.clicked.connect(self.on_start_clicked)
        self.start_progress = QProgressBar()
        self.start_progress.setValue(0)
        self.start_layout.addWidget(self.start_progress)
        self.start_layout.addWidget(self.start_btn)
        self.start_widget.setLayout(self.start_layout)

        self.main_layout.addWidget(self.image_widget)
        self.main_layout.addWidget(self.output_widget)
        self.main_layout.addWidget(self.image_listview)
        self.main_layout.addWidget(self.start_widget)

        self.setLayout(self.main_layout)

    def refresh_images(self, dirname):
        self.image_list_model.clear()
        for path in get_image_files(dirname):
            self.image_list_model.appendRow(QStandardItem(path))

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
        pass
