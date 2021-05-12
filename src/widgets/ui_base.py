from PySide6 import QtCore
from PySide6.QtWidgets import QGridLayout, QWidget


class BaseUI(QWidget):
    def __init__(self, parent=None):
        super(BaseUI, self).__init__(parent)
        self.setup_ui()

    def init_layout(self):
        self.main_layout = QGridLayout()
        self.main_layout.setHorizontalSpacing(10)
        self.main_layout.setVerticalSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setLayout(self.main_layout)

    def setup_ui(self):
        self.init_layout()
