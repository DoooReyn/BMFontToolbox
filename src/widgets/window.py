import os

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QMenu

from src.helper.common import GShortcut, GMenu, GResource, Globals
from src.toolbox.characters import ESCAPE_SWAP_CHARS
from src.widgets.atlas_ui import AtlasUI
from src.widgets.font_ui import FontUI
from src.widgets.message import Message


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon(GResource.icon_window))
        self.init_signal()
        self.init_menu()

    def init_signal(self):
        Globals.signal.msgbox_trigger.connect(self.on_show_msg)
        Globals.signal.open_file_trigger.connect(self.on_show_open_file)
        Globals.signal.mode_trigger.connect(self.on_change_mode)

    def init_menu(self):
        self.add_menu(GMenu.help, [
            (GResource.icon_manual, GShortcut.manual[0], GShortcut.manual[1], self.on_view_manual)
        ])

    def add_menu(self, title, actions):
        menu = QMenu()
        menu.setTitle(title)
        for item in actions:
            icon, name, key, callback = item
            action = QAction(QIcon(icon), name, self)
            if key:
                action.setShortcut(key)
            if callback:
                action.triggered.connect(callback)
            menu.addAction(action)
        self.menuBar().addMenu(menu)

    def open(self):
        self.on_change_mode("mode_1")

    def on_change_mode(self, mode):
        if mode == "mode_1":
            self.setCentralWidget(AtlasUI())
        elif mode == "mode_2":
            self.setCentralWidget(FontUI())

    def closeEvent(self, event):
        Globals.config.set(Globals.UserData.window_width, self.width())
        Globals.config.set(Globals.UserData.window_height, self.height())
        Globals.config.save()
        event.accept()

    @staticmethod
    def on_view_manual():
        tail = ""
        for key, val in ESCAPE_SWAP_CHARS.items():
            tail += "\n\t%s\t=>\t%s" % (key, val)
        Message.show_info(Globals.help + tail, Globals.main_window)

    def on_show_msg(self, msg):
        if Globals.signal.msgbox_trigger and msg:
            Message.show_info(msg, self)

    @staticmethod
    def open_file(msg):
        QDesktopServices.openUrl(QUrl("file:///" + msg))
        QDesktopServices.openUrl(QUrl("file:///" + os.path.dirname(msg)))

    @staticmethod
    def on_show_open_file(msg):
        if Globals.signal.open_file_trigger and msg:
            def callback():
                MainWindow.open_file(msg)

            Message.show_choice(
                msg + "\n\n转换完成！是否打开？",
                "打开",
                "关闭",
                callback
            )

    @staticmethod
    def on_mode_1():
        Globals.signal.mode_trigger.emit("mode_1")

    @staticmethod
    def on_mode_2():
        Globals.signal.mode_trigger.emit("mode_2")
