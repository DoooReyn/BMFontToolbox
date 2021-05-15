import os
import sys

from PySide6.QtCore import Qt, QByteArray, QBuffer
from PySide6.QtGui import QIcon, QAction, QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QMenu, QDockWidget

from helper.common import GShortcut, GMenu, GResource, Globals
from helper.path import clean_app_cache_dir, get_app_cache_dir, open_file_url
from toolbox.characters import ESCAPE_SWAP_CHARS
from widgets.atlas_ui import AtlasUI
from widgets.font_ui import FontUI
from widgets.message import Message
from widgets.setting_ui import SettingUI
import helper.resources


def iconFromBase64(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64))
    icon = QIcon(pixmap)
    return icon


def Base64ToBytes(filename):
    image = QImage(filename)
    ba = QByteArray()
    buff = QBuffer(ba)
    image.save(buff, "PNG")
    return ba.toBase64().data()

image_base64 = b'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'



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.atlas_dock = None
        self.font_dock = None
        self.current_mode = Globals.Mode.setting.value
        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(iconFromBase64(image_base64))
        # icon_path = os.path.join(Globals.app_dir, "static/app.ico")
        # icon_b64 = Base64ToBytes(icon_path)
        # print(icon_b64)
        # print(icon_path)
        # self.setWindowIcon(iconFromBase64(icon_b64))
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
