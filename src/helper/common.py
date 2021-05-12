from enum import Enum

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QLayout


def clear_widgets(layout: QLayout = None):
    if layout is not None:
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()


class GSignal(QObject):
    err_trigger = Signal(str)
    msg_trigger = Signal(str)
    msgbox_trigger = Signal(str)
    export_trigger = Signal()
    open_file_trigger = Signal(str)
    mode_trigger = Signal(int)


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# 全局参数
class GMenu:
    help = "文件"
    mode = "模式"
    # run = "运行"
    # preference = "首选项"


class GShortcut:
    manual = ["手册", "F1"]
    about = ["关于", "F2"]
    about_qt = ["关于Qt", "F3"]
    export = ["导出", "Ctrl+E"]
    mode_1 = ["配置模式", "Ctrl+1"]
    mode_2 = ["图集模式", "Ctrl+2"]
    mode_3 = ["字体模式", "Ctrl+3"]


class GResource:
    icon_window = "resources:icon.svg"
    icon_manual = "resources:notes.svg"
    icon_help = "resources:help.svg"


class Globals:
    class UserData:
        """用户数据存储项key值"""
        images_dir = "images_dir"
        output_dir = "output_dir"
        custom_dir = "custom_dir"
        import_text_dir = "import_text_dir"
        window_width = "window_width"
        window_height = "window_height"
        max_width_index = "max_width_index"
        font_size = "font_size"

    class Mode(Enum):
        """模式枚举（主要页面）"""
        setting = 0
        atlas = 1
        font = 2

    # 帮助文案
    help = r"""
    BMFontGenerator
    
    BMFontGenerator是一款基于Python3和PIL的图片字生成器。
    当前仅支持从图片生成FNT字体，未来将支持TTF、OTF等字体文件。
    
    注意：
    · 使用时，将图片字放在指定目录，并命名为单字符对应的名称；
    · 部分特殊字符无法作为文件名，需要进行替换，规则如下：
    """

    # 最大宽度可选值
    max_width_arr = ["128", "256", "512", "1024", "2048", "4096"]

    # 全局应用变量存点
    app = None

    # 全局主窗口存点
    main_window = None

    # 全局配置存点
    config = None

    # 全局新号存点
    signal = GSignal()

    @staticmethod
    def get_max_width():
        """获取最大宽度值"""
        return int(Globals.max_width_arr[Globals.config.get(Globals.UserData.max_width_index)])

    @staticmethod
    def call(cb, **kwargs):
        """调用方法"""
        if cb:
            cb(**kwargs)
