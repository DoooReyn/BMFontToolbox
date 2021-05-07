from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow

from src.helper.common import GShortcut, GMenu, g_help, GResource, g_signal
from src.toolbox.characters import ESCAPE_SWAP_CHARS
from src.widgets.mainui import MainUI
from src.widgets.message import Message


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon(GResource.icon_window))

        g_signal.msgbox_trigger.connect(self.on_show_msg)
        g_signal.open_file_trigger.connect(self.on_show_open_file)

        self.help_menu = self.menuBar().addMenu(GMenu.help)
        (manual_name, manual_key) = GShortcut.manual
        manual_action = self.create_action(GResource.icon_manual, manual_name, manual_key, self.on_view_manual)
        self.help_menu.addAction(manual_action)

        self.run_menu = self.menuBar().addMenu(GMenu.run)
        (execute_name, execute_key) = GShortcut.execute
        execute_action = self.create_action(GResource.icon_manual, execute_name, execute_key, self.on_execute)
        self.run_menu.addAction(execute_action)

        self.setCentralWidget(MainUI(self.app))

    def create_action(self, icon=None, text="", shortcut=None, on_clicked=None):
        action = QAction(QIcon(icon), text, self)
        if shortcut:
            action.setShortcut(shortcut)
        if on_clicked:
            action.triggered.connect(on_clicked)
        return action

    def closeEvent(self, event):
        self.app.config.set("window_width", self.width())
        self.app.config.set("window_height", self.height())
        self.app.config.save()
        event.accept()

    def on_view_manual(self):
        tail = ""
        for key, val in ESCAPE_SWAP_CHARS.items():
            tail += "\n\t%s\t=>\t%s" % (key, val)
        Message.show_info(g_help + tail, self)

    def on_show_msg(self, msg):
        if g_signal.msgbox_trigger and msg:
            Message.show_info(msg, self)

    @staticmethod
    def on_show_open_file(msg):
        if g_signal.open_file_trigger and msg:
            Message.show_file(msg)

    @staticmethod
    def on_execute():
        g_signal.execute_trigger.emit()
