import os

from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QLabel, QLineEdit, QListView, QPushButton, QFileDialog

from src.helper.common import Globals
from src.helper.path import get_image_files
from src.toolbox.font import FontFactory, FontMode
from src.widgets.message import Message
from src.widgets.ui_base import BaseUI


class AtlasUI(BaseUI):

    def __init__(self):
        self.image_line_edit = None
        self.image_listview = None
        self.image_list_model = None
        self.image_atlas = []
        Globals.signal.export_trigger.connect(self.on_start_clicked)
        super(AtlasUI, self).__init__()

    def setup_ui(self):
        super(AtlasUI, self).setup_ui()

        image_label = QLabel(text="图集目录")
        image_line_edit = QLineEdit(Globals.config.get(Globals.UserData.images_dir))
        image_choose_btn = QPushButton(text="浏览")
        image_choose_btn.clicked.connect(self.on_image_choose_clicked)

        image_listview = QListView()
        image_list_model = QStandardItemModel(image_listview)
        image_list_model.itemChanged.connect(self.on_image_changed)
        image_listview.setModel(image_list_model)

        self.main_layout.addWidget(image_label, 1, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.main_layout.addWidget(image_line_edit, 1, 1, 1, 1)
        self.main_layout.addWidget(image_choose_btn, 1, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.main_layout.addWidget(image_listview, 2, 0, 1, 3)

        self.image_line_edit = image_line_edit
        self.image_listview = image_listview
        self.image_list_model = image_list_model

        self.refresh_images()

    def refresh_images(self):
        self.image_list_model.clear()
        self.image_atlas.clear()
        dirname = self.get_image_dir()
        for path in get_image_files(dirname):
            item = QStandardItem(os.path.splitext(path)[0])
            self.image_list_model.appendRow(item)
            self.image_atlas.append(os.path.join(dirname, path))

    def on_image_choose_clicked(self):
        where = Globals.config.get(Globals.UserData.images_dir)
        url = QFileDialog().getExistingDirectory(dir=where)
        if url is not None and url != "":
            dirname = os.path.abspath(url)
            Globals.config.set(Globals.UserData.images_dir, dirname)
            self.image_line_edit.setText(dirname)
            self.refresh_images()

    def on_image_changed(self, item):
        row = item.index().row()
        old = self.image_atlas[row]
        new = os.path.join(self.get_image_dir(), item.text() + ".png")
        try:
            os.renames(old, new)
            self.image_atlas[row] = new
        except Exception as e:
            Message.show_error(str(e), self)
            item.setText(os.path.splitext(os.path.basename(old))[0])

    def get_image_dir(self):
        return self.image_line_edit.text()

    def on_start_clicked(self):
        if not self.isEnabled() or not self.isVisible():
            return

        from_dir = self.get_image_dir()
        if not (os.path.exists(from_dir) and os.path.isdir(from_dir)):
            Message.show_error("无效的图集目录！", self)
            return

        output_dir = Globals.config.get(Globals.UserData.output_dir)
        if not (os.path.exists(output_dir) and os.path.isdir(output_dir)):
            Message.show_error("无效的输出目录！", self)
            return

        if len(self.image_atlas) <= 0:
            Message.show_error("图集目录下未找到有效图集！", self)
            return

        FontFactory.run_with(FontMode.Atlas, {
            "image": self.image_line_edit.text(),
            "output": output_dir,
            "atlas": self.image_atlas,
            "max_width": Globals.get_max_width()
        })
