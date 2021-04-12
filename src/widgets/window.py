from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow

from .mainui import MainUI
from .manual import Manual


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("BMFont Toolbox")
        self.setWindowIcon(QIcon("resources:icon.svg"))

        self.help_menu = self.menuBar().addMenu("&帮助")
        view_help_action = self.create_action("resources:notes.svg", "&手册", "F1", self.on_view_manual)
        self.help_menu.addAction(view_help_action)

        self.setCentralWidget(MainUI(app))

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
        dialog = Manual(self)
        dialog.show()
        dialog.setFixedSize(320, self.height())
        x, y = self.x(), self.y()
        dialog.move(x + self.width(), y)
