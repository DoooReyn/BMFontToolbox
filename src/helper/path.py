import os
import sys
from shutil import rmtree

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from getfontname import get_font_name


def get_temp_path():
    return os.environ.get("TEMP")


def get_app_cache_dir():
    return os.path.join(get_temp_path(), "bmfont")


def get_user_root():
    return os.environ.get("USERPROFILE")


def get_user_picture():
    return os.path.abspath(os.path.join(get_user_root(), "Pictures"))


def get_user_document():
    return os.path.abspath(os.path.join(get_user_root(), "Documents"))


def get_ext_name(path):
    return os.path.splitext(path)[-1]


def is_ext_matched(path, ext):
    return get_ext_name(path).lower() == ext.lower()


def get_image_files(path):
    files = []
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if is_ext_matched(filename, ".png"):
                files.append(filename)
    return files


def get_system_fonts():
    root = None
    fonts = []
    if sys.platform == "win32":
        root = "C:/Windows/Fonts"
    if root:
        for item in os.listdir(root):
            if item.lower().endswith(".ttf") | item.lower().endswith(".otf"):
                where = os.path.join(root, item)
                names = get_font_name(where)
                family = names[0][0]
                mode = str(names[1][0])
                if mode.lower().find("italic") == -1:
                    name = "%s %s" % (family, mode)
                    font = (where, name, family, mode)
                    fonts.append(font)
    return fonts


def clean_app_cache_dir():
    root = get_app_cache_dir()
    for d in os.listdir(root):
        rmtree(os.path.join(root, d), ignore_errors=True)


def open_file_url(url):
    QDesktopServices.openUrl(QUrl("file:///" + url))
