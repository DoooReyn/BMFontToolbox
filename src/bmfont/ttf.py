# -*- coding: utf-8 -*-
# coding: utf-8

import os
import sys
from PIL import ImageDraw, ImageFont, Image
from fontTools.ttLib import TTFont
from constant import SPECIAL_SWAP_CHARACTERS
from shutil import rmtree


class BMFontTTF:
    def __init__(self, ttf, chars="", size=32, stroke_color=None, stroke_width=0):
        self.size = size
        self.chars = None
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.ttf = None
        self.glyf = None
        self.font = None
        self.__check_ttf(ttf)
        self.__check_chars(chars)

    def __check_ttf(self, ttf):
        if os.path.isfile(ttf) and (os.path.splitext(ttf)[-1]).lower() == ".ttf":
            self.ttf = ttf
            self.glyf = TTFont(ttf).getBestCmap()
            self.font = ImageFont.truetype(ttf, self.size)
        else:
            print("找不到字体: %s" % ttf)
            sys.exit(-1)

    def __check_chars(self, text):
        chars = []
        arr = list(set(list(text)))
        for char in arr:
            if self.has_char(char):
                chars.append(char)
        if len(chars) == 0:
            print("找不到有效的输入字符")
            sys.exit(-1)
        self.chars = sorted(chars)
        self.chars.append(u"\u0020")

    def has_char(self, char):
        try:
            return self.glyf.get(ord(char)) is not None
        except Exception:
            print("无效的字符: %s" % char)
            return False

    def save(self, path):
        if path is None:
            print("无效的保存位置: %s" % str(path))
            sys.exit(-1)
        os.makedirs(path, exist_ok=True)
        if not os.path.isdir(path):
            print("无效的保存位置: %s" % str(path))
            sys.exit(-1)
        else:
            rmtree(path, ignore_errors=True)
            os.makedirs(path, exist_ok=True)

        channel = (0, 0, 0, 0)
        for char in self.chars:
            size = self.font.getsize(char, stroke_width=self.stroke_width)
            size2 = self.font.getsize(char)
            offset = ((size[0] - size2[0]), (size[1] - size2[1]))
            # size = (size[0] + offset[0], size[1] + offset[1])
            image = Image.new("RGBA", size, channel)
            draw = ImageDraw.Draw(image)
            draw.text(offset, char, font=self.font, spacing=0,
                      stroke_fill=self.stroke_color, stroke_width=self.stroke_width)
            repl = SPECIAL_SWAP_CHARACTERS.get(char)
            repl = repl or char
            image.save(os.path.join(path, "%s.png" % repl))
            print("正在添加字符: %s" % char)


if __name__ == "__main__":
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bmfont = BMFontTTF(r"E:/Libary/2-Asset/22-Font/JetBrainsMono-Regular.ttf", chars, stroke_color="#666666", stroke_width=2)
    bmfont.save("./output/JetBrainsMono-Regular")