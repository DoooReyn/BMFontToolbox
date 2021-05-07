import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication

from src.helper.common import (SingletonMeta)
from src.helper.config import (Config)
from src.helper.path import (get_user_picture, get_user_document)
from src.widgets.window import MainWindow


class App(metaclass=SingletonMeta):
    config = Config("bmfont_toolbox_config.json")

    def __init__(self):
        self.instance = QApplication([])
        App.config.init("images", get_user_picture())
        App.config.init("output", get_user_document())
        App.config.init("window_width", 640)
        App.config.init("window_height", 480)
        QDir.addSearchPath("resources", "../static/")

    def run(self, width=640, height=480):
        window = MainWindow(self)
        width = App.config.get_default("window_width", width)
        height = App.config.get_default("window_height", height)
        window.resize(width, height)
        window.show()
        sys.exit(self.instance.exec_())
