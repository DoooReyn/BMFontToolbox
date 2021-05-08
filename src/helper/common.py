from PySide6.QtCore import QObject, Signal


class GSignal(QObject):
    err_trigger = Signal(str)
    msg_trigger = Signal(str)
    msgbox_trigger = Signal(str)
    execute_trigger = Signal()
    open_file_trigger = Signal(str)


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
    help = "&帮助"
    run = "&运行"


class GShortcut:
    manual = ["&手册", "F1"]
    execute = ["&转换", "F5"]


class GResource:
    icon_window = "resources:icon.svg"
    icon_manual = "resources:notes.svg"
    icon_help = "resources:help.svg"


class Globals:
    help = r"""
    BMFontGenerator
    
    BMFontGenerator是一款基于Python3和PIL的图片字生成器。
    当前仅支持从图片生成FNT字体，未来将支持TTF、OTF等字体文件。
    
    注意：
    · 使用时，将图片字放在指定目录，并命名为单字符对应的名称；
    · 部分特殊字符无法作为文件名，需要进行替换，规则如下：
    """

    signal = GSignal()

    @staticmethod
    def call(cb, **kwargs):
        if cb:
            cb(**kwargs)

