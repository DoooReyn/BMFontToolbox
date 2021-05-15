import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QMenu, QDockWidget

from helper.common import GShortcut, GMenu, GResource, Globals
from helper.path import clean_app_cache_dir, get_app_cache_dir, open_file_url
from toolbox.characters import ESCAPE_SWAP_CHARS
from widgets.atlas_ui import AtlasUI
from widgets.font_ui import FontUI
from widgets.message import Message
from widgets.setting_ui import SettingUI
import helper.resources


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.atlas_dock = None
        self.font_dock = None
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
        self.add_menu(GMenu.file, [
            (None, GShortcut.export[0], GShortcut.export[1], self.on_export),
            (None, GShortcut.open_app_dir[0], GShortcut.open_app_dir[1], self.on_open_app_dir),
            (None, GShortcut.clean[0], GShortcut.clean[1], self.on_clean_app_dir)
        ])
        self.add_menu(GMenu.help, [
            (GResource.icon_manual, GShortcut.manual[0], GShortcut.manual[1], self.on_view_manual),
            (None, GShortcut.about[0], GShortcut.about[1], self.on_view_about),
            (None, GShortcut.about_qt[0], GShortcut.about_qt[1], self.on_view_about_qt)
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
        cw = self.centralWidget()
        if cw:
            cw.hide()

        setting_dock = QDockWidget("基础配置", self)
        setting_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        setting_dock.setWidget(SettingUI())
        setting_dock.setMaximumHeight(120)
        self.addDockWidget(Qt.TopDockWidgetArea, setting_dock)

        atlas_dock = QDockWidget("图集模式", self)
        atlas_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        atlas_dock.setWidget(AtlasUI())
        atlas_dock.setEnabled(True)
        self.atlas_dock = atlas_dock
        self.addDockWidget(Qt.BottomDockWidgetArea, atlas_dock)

        font_dock = QDockWidget("字体模式", self)
        font_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        font_dock.setWidget(FontUI())
        font_dock.setEnabled(False)
        font_dock.hide()
        self.font_dock = font_dock
        self.addDockWidget(Qt.BottomDockWidgetArea, font_dock)

    def on_change_mode(self, mode):
        self.atlas_dock.setEnabled(mode == Globals.Mode.atlas.value)
        self.font_dock.setEnabled(mode == Globals.Mode.font.value)
        self.atlas_dock.setVisible(mode == Globals.Mode.atlas.value)
        self.font_dock.setVisible(mode == Globals.Mode.font.value)

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

    @staticmethod
    def on_clean_app_dir():
        clean_app_cache_dir()

    @staticmethod
    def on_open_app_dir():
        open_file_url(get_app_cache_dir())

    def on_show_msg(self, msg):
        if Globals.signal.msgbox_trigger and msg:
            Message.show_info(msg, self)

    @staticmethod
    def open_file(msg):
        open_file_url(msg)
        open_file_url(os.path.dirname(msg))

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
