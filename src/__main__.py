import os
import sys

from PySide6.QtWidgets import QApplication

from helper.common import Globals
from helper.config import Config
from helper.path import get_user_picture, get_user_document
from widgets.window import MainWindow


# import PySide6
# dirname = os.path.dirname(PySide6.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# print(plugin_path)


def app_path():
    ret = None
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        ret = os.path.dirname(sys.executable)
    ret = os.path.dirname(__file__)
    return os.path.abspath(ret)


if __name__ == "__main__":
    Globals.app = QApplication([])
    Globals.app_dir = app_path()
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
    Globals.main_window = MainWindow()
    Globals.main_window.resize(Globals.config.get(Globals.UserData.window_width),
                               Globals.config.get(Globals.UserData.window_height))
    Globals.main_window.show()
    Globals.main_window.open()
    sys.exit(Globals.app.exec())
