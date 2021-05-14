import os

from PySide6 import QtCore
from PySide6.QtWidgets import QGridLayout, QWidget

from src.helper.common import Globals
from src.widgets.message import Message


class BaseUI(QWidget):
    def __init__(self, parent=None):
        super(BaseUI, self).__init__(parent)
        self.main_layout = None
        self.setup_ui()

    def init_layout(self):
        self.main_layout = QGridLayout()
        self.main_layout.setHorizontalSpacing(4)
        self.main_layout.setVerticalSpacing(4)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setLayout(self.main_layout)

    def setup_ui(self):
        self.init_layout()

    def check_is_ready(self):
        if not self.isEnabled() or not self.isVisible():
            return False

        output_dir = Globals.config.get(Globals.UserData.output_dir)
        if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
            Message.show_error("无效的输出目录！", self)
            return False

        save_as_path = os.path.join(output_dir, Globals.config.get(Globals.UserData.font_save_name) + ".png")
        if os.path.exists(save_as_path):
            Message.show_error("已存在同名文件！", self)
            return False

        return True
