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

        self.menu_help = self.menuBar().addMenu("&帮助")
        action_manual = QAction(QIcon(), "&手册", self)
        action_manual.setShortcut("F1")
        action_manual.triggered.connect(self.on_view_manual)
        self.action_manual = self.menu_help.addAction(action_manual)

        self.setCentralWidget(MainUI(app))

    def closeEvent(self, event):
        self.app.config.set("window_width", self.width())
        self.app.config.set("window_height", self.height())
        self.app.config.save()
        event.accept()

    def on_view_manual(self):
        dialog = Manual(self)
        dialog.show()
        dialog.setFixedSize(320, self.app.config.get("window_height"))
        x, y = self.x(), self.y()
        dialog.move(x + self.width(), y)
