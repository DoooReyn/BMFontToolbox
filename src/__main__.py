import os
import sys

from PySide6 import QtCore
from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem
)
from PySide6.QtWidgets import (
    QLabel, QLineEdit, QApplication,
    QWidget, QPushButton, QHBoxLayout,
    QVBoxLayout, QFileDialog, QListView
)


def get_image_path():
    return os.path.abspath(os.path.join(os.environ.get("USERPROFILE"), "Pictures"))


def get_output_path():
    return os.path.abspath(os.path.join(os.environ.get("USERPROFILE"), "Documents"))


def get_image_files(path):
    files = []
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if os.path.splitext(filename)[-1] == ".png":
                files.append(filename)
    return files


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)

        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        image_label = QLabel(text='图集目录', alignment=QtCore.Qt.AlignCenter)
        self.image_line_edit = QLineEdit(get_image_path())
        self.image_choose_btn = QPushButton(text='选择')
        self.image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        self.image_layout.addWidget(image_label)
        self.image_layout.addWidget(self.image_line_edit)
        self.image_layout.addWidget(self.image_choose_btn)
        self.image_widget.setLayout(self.image_layout)

        self.output_widget = QWidget()
        self.output_layout = QHBoxLayout()
        output_label = QLabel(text='输出目录', alignment=QtCore.Qt.AlignCenter)
        self.output_line_edit = QLineEdit(get_output_path())
        self.output_choose_btn = QPushButton(text='选择')
        self.output_choose_btn.clicked.connect(self.on_output_choose_clicked)
        self.output_layout.addWidget(output_label)
        self.output_layout.addWidget(self.output_line_edit)
        self.output_layout.addWidget(self.output_choose_btn)
        self.output_widget.setLayout(self.output_layout)

        self.image_listview = QListView()
        self.image_list_model = QStandardItemModel(self.image_listview)
        for path in get_image_files(get_image_path()):
            self.image_list_model.appendRow(QStandardItem(path))
        self.image_listview.setModel(self.image_list_model)

        self.main_layout.addWidget(self.image_widget)
        self.main_layout.addWidget(self.output_widget)
        self.main_layout.addWidget(self.image_listview)

        self.setLayout(self.main_layout)

    def refresh_images(self, dirname):
        self.image_list_model.clear()
        for path in get_image_files(dirname):
            self.image_list_model.appendRow(QStandardItem(path))

    def on_image_choose_clicked(self):
        where = get_image_path()
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            self.image_line_edit.setText(dirname)
            self.refresh_images(dirname)

    def on_output_choose_clicked(self):
        where = get_output_path()
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            self.output_line_edit.setText(os.path.abspath(url))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
