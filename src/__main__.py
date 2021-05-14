import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication

from src.helper.common import Globals
from src.helper.config import Config
from src.helper.path import get_user_picture, get_user_document
from src.widgets.window import MainWindow

if __name__ == "__main__":
    Globals.app = QApplication([])
    Globals.config = Config("bmfont_toolbox_config.json")
    Globals.config.init(Globals.UserData.images_dir, get_user_picture())
    Globals.config.init(Globals.UserData.output_dir, get_user_document())
    Globals.config.init(Globals.UserData.custom_dir, get_user_document())
    Globals.config.init(Globals.UserData.import_text_dir, get_user_document())
    Globals.config.init(Globals.UserData.font_save_name, "font")
    Globals.config.init(Globals.UserData.font_size, 10)
    Globals.config.init(Globals.UserData.window_width, 640)
    Globals.config.init(Globals.UserData.window_height, 480)
    Globals.config.init(Globals.UserData.max_width_index, 1)
    QDir.addSearchPath("resources", "../static/")
    Globals.main_window = MainWindow()
    Globals.main_window.resize(Globals.config.get(Globals.UserData.window_width), Globals.config.get(Globals.UserData.window_height))
    Globals.main_window.show()
    Globals.main_window.open()
    sys.exit(Globals.app.exec_())
