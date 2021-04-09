import os
import sys

from PySide6 import QtCore
from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QIcon,
    QAction
)
from PySide6.QtWidgets import (
    QLabel, QLineEdit, QApplication,
    QWidget, QPushButton, QHBoxLayout,
    QVBoxLayout, QFileDialog, QListView,
    QProgressBar, QMainWindow, QDialog,
    QTextEdit
)

from helper.config import (Config)
from helper.path import (get_user_picture, get_user_document, is_ext_matched)

HELP = r"""
BMFontGenerator

BMFontGenerator是一款基于Python3和PIL的图片字生成器。
当前仅支持从图片生成FNT字体，未来将支持TTF。

注意：
· 使用时，将图片字放在指定目录，并命名为单字符对应的名称；
· 部分特殊字符无法作为文件名，需要进行替换，如：
    : -> 冒号
    ? -> 问号
    * -> 星号
    / -> 斜杠
    \ -> 反斜杠
    > -> 大于
    < -> 小于
    | -> 竖线
    \ -> 引号
· 生成的文件保存在当前目录下的output目录。

使用方法：
python generator.py ./path_to_pictures name_of_output_file
"""


def get_image_files(path):
    files = []
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if is_ext_matched(filename, ".png"):
                files.append(filename)
    return files


def get_resource(filename):
    global resource
    return os.path.join(resource, filename)


class MainUI(QWidget):
    def __init__(self):
        global config
        super(MainUI, self).__init__()

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)

        self.image_widget = QWidget()
        self.image_layout = QHBoxLayout()
        image_label = QLabel(text='图集目录', alignment=QtCore.Qt.AlignCenter)
        self.image_line_edit = QLineEdit(config.get("images"))
        self.image_choose_btn = QPushButton(text='选择')
        self.image_choose_btn.clicked.connect(self.on_image_choose_clicked)
        self.image_layout.addWidget(image_label)
        self.image_layout.addWidget(self.image_line_edit)
        self.image_layout.addWidget(self.image_choose_btn)
        self.image_widget.setLayout(self.image_layout)

        self.output_widget = QWidget()
        self.output_layout = QHBoxLayout()
        output_label = QLabel(text='输出目录', alignment=QtCore.Qt.AlignCenter)
        self.output_line_edit = QLineEdit(config.get("output"))
        self.output_choose_btn = QPushButton(text='选择')
        self.output_choose_btn.clicked.connect(self.on_output_choose_clicked)
        self.output_layout.addWidget(output_label)
        self.output_layout.addWidget(self.output_line_edit)
        self.output_layout.addWidget(self.output_choose_btn)
        self.output_widget.setLayout(self.output_layout)

        self.image_listview = QListView()
        self.image_list_model = QStandardItemModel(self.image_listview)
        for path in get_image_files(config.get("images")):
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
        global config
        where = config.get("images")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            config.set("images", dirname)
            self.image_line_edit.setText(dirname)
            self.refresh_images(dirname)

    def on_output_choose_clicked(self):
        global config
        where = config.get("output")
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            config.set("output", dirname)
            self.output_line_edit.setText(dirname)

    def on_start_clicked(self):
        pass


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        global resource
        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon(get_resource("icon.svg")))

        self.menu_help = self.menuBar().addMenu("&帮助")
        action_manual = QAction(QIcon(), "&手册", self)
        action_manual.setShortcut("F1")
        action_manual.triggered.connect(self.on_view_manual)
        self.action_manual = self.menu_help.addAction(action_manual)

        self.setCentralWidget(MainUI())

    def closeEvent(self, event):
        global config
        config.save()
        event.accept()

    def on_view_manual(self):
        manual_widget = QDialog(parent=self)
        manual_widget.setWindowTitle("手册")
        manual_layout = QVBoxLayout()
        manual_layout.setAlignment(QtCore.Qt.AlignTop)
        text = QTextEdit(text=HELP)
        text.setReadOnly(True)
        manual_layout.addWidget(text)
        manual_widget.setLayout(manual_layout)
        manual_widget.setFixedSize(400, 240)
        manual_widget.show()


if __name__ == "__main__":
    config = Config("bmfont_toolbox_config.json")
    config.init("images", get_user_picture())
    config.init("output", get_user_document())

    app = QApplication([])
    resource = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))
    app.addLibraryPath(resource)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
