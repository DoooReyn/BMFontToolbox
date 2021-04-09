import os
import sys

from PySide6 import QtCore
from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QIcon
)
from PySide6.QtWidgets import (
    QLabel, QLineEdit, QApplication,
    QWidget, QPushButton, QHBoxLayout,
    QVBoxLayout, QFileDialog, QListView,
    QProgressBar
)

from helper.config import (Config)
from helper.path import (get_user_picture, get_user_document, is_ext_matched)


def get_image_files(path):
    files = []
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if is_ext_matched(filename, ".png"):
                files.append(filename)
    return files


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon("../static/icon.svg"))

        self.config = Config("bmfont_toolbox_config.json")
        self.config.init("images", get_user_picture())
        self.config.init("output", get_user_document())

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)

        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        image_label = QLabel(text='图集目录', alignment=QtCore.Qt.AlignCenter)
        self.image_line_edit = QLineEdit(self.config.get("images"))
        self.image_choose_btn = QPushButton(text='选择')
        self.image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        self.image_layout.addWidget(image_label)
        self.image_layout.addWidget(self.image_line_edit)
        self.image_layout.addWidget(self.image_choose_btn)
        self.image_widget.setLayout(self.image_layout)

        self.output_widget = QWidget()
        self.output_layout = QHBoxLayout()
        output_label = QLabel(text='输出目录', alignment=QtCore.Qt.AlignCenter)
        self.output_line_edit = QLineEdit(self.config.get("output"))
        self.output_choose_btn = QPushButton(text='选择')
        self.output_choose_btn.clicked.connect(self.on_output_choose_clicked)
        self.output_layout.addWidget(output_label)
        self.output_layout.addWidget(self.output_line_edit)
        self.output_layout.addWidget(self.output_choose_btn)
        self.output_widget.setLayout(self.output_layout)

        self.image_listview = QListView()
        self.image_list_model = QStandardItemModel(self.image_listview)
        for path in get_image_files(self.config.get("images")):
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
        where = self.config.get("images")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.config.set("images", dirname)
            self.image_line_edit.setText(dirname)
            self.refresh_images(dirname)

    def on_output_choose_clicked(self):
        where = self.config.get("output")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.config.set("output", dirname)
            self.output_line_edit.setText(dirname)

    def closeEvent(self, event):
        self.config.save()
        event.accept()

    def on_start_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    app.addLibraryPath("../static")
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
