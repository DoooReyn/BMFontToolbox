from enum import Enum

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

from helper.common import GResource, Globals


class Level(Enum):
    Info = 0
    Warning = 1
    Error = 2


class Message:
    LEVEL_NAMES = ["提示", "警告", "错误"]

    @staticmethod
    def show_info(text, parent):
        QMessageBox.information(parent, Message.LEVEL_NAMES[Level.Info.value], text)

    @staticmethod
    def show_warning(text, parent):
        QMessageBox.warning(parent, Message.LEVEL_NAMES[Level.Warning.value], text)

    @staticmethod
    def show_error(text, parent):
        QMessageBox.critical(parent, Message.LEVEL_NAMES[Level.Error.value], text)

    @staticmethod
    def show_choice(text="", confirm_text="确认", deny_text="取消", confirm_cb=None, deny_cb=None):
        box = QMessageBox()
        box.setWindowTitle(Message.LEVEL_NAMES[Level.Info.value])
        box.setWindowIcon(QIcon(GResource.icon_window))
        box.setText(text)
        box.addButton(confirm_text, QMessageBox.AcceptRole)
        box.addButton(deny_text, QMessageBox.RejectRole)
        reply = box.exec_()
        if reply == QMessageBox.AcceptRole:
            Globals.call(confirm_cb)
        elif reply == QMessageBox.RejectRole:
            Globals.call(deny_cb)
