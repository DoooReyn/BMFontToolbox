from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow

from src.widgets.mainui import MainUI
from src.widgets.message import Message


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon("resources:icon.svg"))

        self.help_menu = self.menuBar().addMenu("&帮助")
        view_help_action = self.create_action("resources:notes.svg", "&手册", "F1", self.on_view_manual)
        self.help_menu.addAction(view_help_action)

        self.setCentralWidget(MainUI(self.app))

    def create_action(self, icon=None, text="", shortcut=None, on_clicked=None):
        action = QAction(QIcon(icon), text, self)
        if shortcut:
            action.setShortcut(shortcut)
        if on_clicked:
            action.triggered.connect(on_clicked)
        return action

    def closeEvent(self, event):
        self.app.config.set("window_width", self.width())
        self.app.config.set("window_height", self.height())
        self.app.config.save()
        event.accept()

    def on_view_manual(self):
        Message.show_info(HELP, self)


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
