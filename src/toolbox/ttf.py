import os
from datetime import datetime

from PIL import ImageDraw, ImageFont, Image
from fontTools.ttLib import TTFont

from helper.common import Globals
from helper.path import get_app_cache_dir
from toolbox.atlas import Atlas
from toolbox.characters import ESCAPE_SWAP_CHARS


class BMFontTTF:
    def __init__(self, ttf, chars="", size=32, stroke_color=None, stroke_width=0):
        self.size = size
        self.chars = None
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.ttf = None
        self.glyf = None
        self.font = None
        if self.__check_ttf(ttf):
            self.__check_chars(chars)

    def __check_ttf(self, ttf):
        if os.path.isfile(ttf) and (os.path.splitext(ttf)[-1]).lower() == ".ttf":
            self.ttf = ttf
            self.glyf = TTFont(ttf).getBestCmap()
            self.font = ImageFont.truetype(ttf, self.size)
        else:
            print("找不到字体: %s" % ttf)
            return False
        if not self.glyf or not self.font:
            print("无效的字体: %s" % ttf)
            return False
        return True

    def __check_chars(self, text):
        chars = []
        arr = list(set(list(text)))
        for char in arr:
            if self.has_char(char):
                chars.append(char)
        if len(chars) == 0:
            print("找不到有效的输入字符")
            return False
        self.chars = sorted(chars)
        self.chars.append(u"\u0020")
        return True

    def has_char(self, char):
        try:
            return self.glyf.get(ord(char)) is not None
        except Exception:
            print("无效的字符: %s" % char)
            return False

    def save(self, path, save_file):
        if path is None:
            print("无效的保存位置: %s" % str(path))
            return
        os.makedirs(path, exist_ok=True)
        if not os.path.isdir(path):
            print("无效的保存位置: %s" % str(path))
            return
        else:
            # rmtree(path, ignore_errors=True)
            os.makedirs(path, exist_ok=True)

        if not self.chars or len(self.chars) == 0:
            return

        channel = (0, 0, 0, 0)
        files = []
        from_path = os.path.join(get_app_cache_dir(), datetime.now().strftime("%Y%m%d%H%M%S"))
        os.makedirs(from_path, exist_ok=True)
        for char in self.chars:
            size = self.font.getsize(char, stroke_width=self.stroke_width)
            size2 = self.font.getsize(char)
            offset = ((size[0] - size2[0]), (size[1] - size2[1]))
            # size = (size[0] + offset[0], size[1] + offset[1])
            image = Image.new("RGBA", size, channel)
            draw = ImageDraw.Draw(image)
            draw.text(offset, char, font=self.font, spacing=0,
                      stroke_fill=self.stroke_color, stroke_width=self.stroke_width)
            repl = ESCAPE_SWAP_CHARS.get(char)
            repl = repl or char
            print("TTF正在添加字符: %s => %s" % (char, repl))
            filename = os.path.join(from_path, "%s.png" % repl)
            image.save(filename)
            files.append(filename)

        Atlas({
            "image": from_path,
            "output": path,
            "atlas": files,
            "max_width": Globals.get_max_width(),
            "save_file": save_file
        }).generate()


class TTF:
    def __init__(self, configuration: dict):
        self.configuration = configuration

    def generate(self):
        where = self.configuration.get("where")
        chars = self.configuration.get("chars")
        output = self.configuration.get("output")
        font_size = self.configuration.get("font_size")
        save_file = self.configuration.get("save_file")
        BMFontTTF(ttf=where, chars=chars, size=font_size).save(output, save_file)
