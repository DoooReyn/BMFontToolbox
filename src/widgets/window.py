import os

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QMenu

from src.helper.common import GShortcut, GMenu, GResource, Globals
from src.toolbox.characters import ESCAPE_SWAP_CHARS
from src.widgets.atlas_ui import AtlasUI
from src.widgets.font_ui import FontUI
from src.widgets.message import Message
from src.widgets.setting_ui import SettingUI


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_mode = Globals.Mode.setting.value
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
            (None, GShortcut.export[0], GShortcut.export[1], self.on_export),
            (GResource.icon_manual, GShortcut.manual[0], GShortcut.manual[1], self.on_view_manual),
            (None, GShortcut.about[0], GShortcut.about[1], self.on_view_about),
            (None, GShortcut.about_qt[0], GShortcut.about_qt[1], self.on_view_about_qt)
        ])
        self.add_menu(GMenu.mode, [
            (None, GShortcut.mode_1[0], GShortcut.mode_1[1], self.on_change_to_mode_1),
            (None, GShortcut.mode_2[0], GShortcut.mode_2[1], self.on_change_to_mode_2),
            (None, GShortcut.mode_3[0], GShortcut.mode_3[1], self.on_change_to_mode_3)
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
        self.on_change_mode(self.current_mode)

    def on_change_to_mode_1(self):
        if self.current_mode != Globals.Mode.setting.value:
            self.current_mode = Globals.Mode.setting.value
            self.on_change_mode(self.current_mode)

    def on_change_to_mode_2(self):
        if self.current_mode != Globals.Mode.atlas.value:
            self.current_mode = Globals.Mode.atlas.value
            self.on_change_mode(self.current_mode)

    def on_change_to_mode_3(self):
        if self.current_mode != Globals.Mode.font.value:
            self.current_mode = Globals.Mode.font.value
            self.on_change_mode(self.current_mode)

    def on_change_mode(self, mode):
        widget = None
        if mode == Globals.Mode.atlas.value:
            widget = AtlasUI()
        elif mode == Globals.Mode.font.value:
            widget = FontUI()
        elif mode == Globals.Mode.setting.value:
            widget = SettingUI()
        if widget:
            self.setCentralWidget(widget)

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

    def on_view_about(self):
        pass

    def on_view_about_qt(self):
        pass

    @staticmethod
    def on_export():
        Globals.signal.export_trigger.emit()

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
