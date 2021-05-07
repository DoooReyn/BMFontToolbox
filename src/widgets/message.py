import os
from enum import Enum

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import QMessageBox

from src.helper.common import GResource, call


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
    def show_file(text):
        def open_file():
            QDesktopServices.openUrl(QUrl("file:///" + text))
            QDesktopServices.openUrl(QUrl("file:///" + os.path.dirname(text)))

        Message.show_choice(
            text + "\n\n转换完成！是否打开？",
            "打开",
            "关闭",
            open_file
        )

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
            call(confirm_cb)
        elif reply == QMessageBox.RejectRole:
            call(deny_cb)
