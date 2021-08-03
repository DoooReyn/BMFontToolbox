from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from helper.common import Globals
from helper.resources import GRes, GMakeIcon


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.main_layout = None
        self.setWindowTitle("关于")
        self.setWindowIcon(GMakeIcon(GRes.app_icon_ico))
        self.setFixedSize(320, 240)
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setLayout(self.main_layout)

        name = '<a href="%s"><b><font size="4" color="#333">%s</font></b></a>' % (Globals.repo, Globals.app_name)
        version = '<b><font size="3" color="#333">版本：</font></b>%s' % Globals.version
        author = '<b><font size="3" color="#333">作者：</font></b>%s' % Globals.author
        tech = '<b><font size="3" color="#333">技术：</font></b>'
        name_lab = QLabel(name)
        name_lab.setOpenExternalLinks(True)
        self.main_layout.addWidget(name_lab)
        self.main_layout.addWidget(QLabel(version))
        self.main_layout.addWidget(QLabel(author))
        self.main_layout.addWidget(QLabel(tech))
        for t in Globals.tech.split('\n'):
            self.main_layout.addWidget(QLabel('<font color="#444">  %s</font>' % t))
