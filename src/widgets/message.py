from enum import Enum

from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel


class Level(Enum):
    Info = "Info"
    Warning = "Warning"
    Error = "Error"


class Message:
    def __init__(self):
        pass

    @staticmethod
    def show_dialog(parent, title, tip):
        dialog = QDialog(parent)
        dialog.setWindowTitle(title)
        dialog.setFixedSize(160, 100)
        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        dialog.setLayout(layout)
        layout.addWidget(QLabel(tip))
        dialog.show()

    @staticmethod
    def show_info(text, parent):
        Warning.show_dialog(parent, Level.Info, text)

    @staticmethod
    def show_warning(text, parent):
        Warning.show_dialog(parent, Level.Warning, text)

    @staticmethod
    def show_error(text, parent):
        Warning.show_dialog(parent, Level.Error, text)
