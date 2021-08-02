import os

from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QLabel, QLineEdit, QListView, QPushButton, QFileDialog

from helper.common import Globals
from helper.path import get_image_files
from toolbox.font import FontFactory, FontMode
from widgets.message import Message
from widgets.ui_base import BaseUI


class AtlasUI(BaseUI):

    def __init__(self):
        self.image_clear_btn = None
        self.image_listview = None
        self.image_list_model = None
        self.image_atlas = []
        self.image_atlas_set = set()
        Globals.signal.export_trigger.connect(self.on_start_clicked)
        super(AtlasUI, self).__init__()
        self.setAcceptDrops(True)

    def setup_ui(self):
        super(AtlasUI, self).setup_ui()

        image_clear_btn = QPushButton(text="清空")
        image_clear_btn.clicked.connect(self.on_image_clear_btn_clicked)

        image_listview = QListView()
        image_listview.setAcceptDrops(True)
        image_list_model = QStandardItemModel(image_listview)
        image_list_model.itemChanged.connect(self.on_image_changed)
        image_listview.setModel(image_list_model)

        self.main_layout.addWidget(image_clear_btn, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(image_listview, 1, 0, 1, 1)

        self.image_clear_btn = image_clear_btn
        self.image_listview = image_listview
        self.image_list_model = image_list_model

        self.refresh_images()

    def on_image_clear_btn_clicked(self):
        self.image_atlas_set.clear()
        self.image_list_model.clear()

    def dragEnterEvent(self, e):
        ok = False
        for url in e.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path) and path.lower().endswith('.png'):
                self.image_atlas_set.add(path)
                ok = True
                e.accept()
            else:
                e.ignore()
        if ok:
            self.refresh_images()

    def refresh_images(self):
        self.image_list_model.clear()

        for path in list(self.image_atlas_set):
            item = QStandardItem(os.path.basename(path))
            self.image_list_model.appendRow(item)

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

    def on_start_clicked(self):
        if not self.check_is_ready():
            return

        if len(self.image_atlas_set) <= 0:
            Message.show_error("图集目录下未找到有效图集！", self)
            return

        output_dir = Globals.config.get(Globals.UserData.output_dir)
        save_file = Globals.config.get(Globals.UserData.font_save_name)
        FontFactory.run_with(FontMode.Atlas, {
            "output": output_dir,
            "save_file": save_file,
            "atlas": list(self.image_atlas_set),
            "max_width": Globals.get_max_width()
        })
