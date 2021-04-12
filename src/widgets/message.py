from enum import Enum

from PySide6.QtWidgets import QMessageBox


class Level(Enum):
    Info = 0
    Warning = 1
    Error = 2


LEVEL_NAMES = ["提示", "警告", "错误"]


class Message:
    @staticmethod
    def show_info(text, parent):
        QMessageBox.information(parent, LEVEL_NAMES[Level.Info.value], text)

    @staticmethod
    def show_warning(text, parent):
        QMessageBox.warning(parent, LEVEL_NAMES[Level.Warning.value], text)

    @staticmethod
    def show_error(text, parent):
        QMessageBox.critical(parent, LEVEL_NAMES[Level.Error.value], text)
