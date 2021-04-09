from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit

HELP = r"""
BMFontGenerator

BMFontGenerator是一款基于Python3和PIL的图片字生成器。
当前仅支持从图片生成FNT字体，未来将支持TTF。

注意：
· 使用时，将图片字放在指定目录，并命名为单字符对应的名称；
· 部分特殊字符无法作为文件名，需要进行替换，如：
    : -> 冒号
    ? -> 问号
    * -> 星号
    / -> 斜杠
    \ -> 反斜杠
    > -> 大于
    < -> 小于
    | -> 竖线
    \ -> 引号
· 生成的文件保存在当前目录下的output目录。

使用方法：
python generator.py ./path_to_pictures name_of_output_file
"""


class Manual(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("手册")
        manual_layout = QVBoxLayout()
        manual_layout.setAlignment(QtCore.Qt.AlignTop)
        text = QTextEdit(text=HELP)
        text.setReadOnly(True)
        manual_layout.addWidget(text)
        self.setLayout(manual_layout)
