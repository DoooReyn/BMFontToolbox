# -*- coding: utf-8 -*-
# coding: utf-8

import os
import sys
from enum import Enum

from PIL import Image

from constant import SPECIAL_CHARACTERS

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

TOP_ALIGNMENT_SYMBOL = {u"^", u"`", u'"', u"'", u"”", u"“"}
BOTTOM_ALIGNMENT_SYMBOL = {u",", u".", u"_", u"…", u"，", u"。"}


def show_help():
    print(HELP)


class FntInfo:
    """
    tag: info

    This tag holds information on how the font was generated.

    face	    This is the name of the true type font.
    size	    The size of the true type font.
    bold	    The font is bold.
    italic	    The font is italic.
    charset	    The name of the OEM charset used (when not unicode).
    unicode	    Set to 1 if it is the unicode charset.
    stretchH	The font height stretch in percentage. 100% means no stretch.
    smooth	    Set to 1 if smoothing was turned on.
    aa	        The supersampling level used. 1 means no supersampling was used.
    padding	    The padding for each character (up, right, down, left).
    spacing	    The spacing for each character (horizontal, vertical).
    outline	    The outline thickness for the characters.
    """

    def __init__(self):
        self.face = ""
        self.size = 32
        self.bold = 0
        self.italic = 0
        self.charset = ""
        self.unicode = 1
        self.stretch_h = 100
        self.smooth = 1
        self.aa = 1
        self.padding = "0,0,0,0"
        self.spacing = "0,0"
        self.outline = 0

    def text(self):
        return "info face=\"%s\" size=%s bold=%s italic=%s charset=\"%s\" unicode=%s stretchH=%s smooth=%s aa=%s padding=%s spacing=%s outline=%s" % (
            self.face, self.size, self.bold, self.italic, self.charset,
            self.unicode, self.stretch_h, self.smooth, self.aa, self.padding,
            self.spacing, self.outline
        )


class FntCommon:
    """
    tag: common

    This tag holds information common to all characters.

    lineHeight	This is the distance in pixels between each line of text.
    base	    The number of pixels from the absolute top of the line to the base of the characters.
    scaleW	    The width of the texture, normally used to scale the x pos of the character image.
    scaleH	    The height of the texture, normally used to scale the y pos of the character image.
    pages	    The number of texture pages included in the font.
    packed	    Set to 1 if the monochrome characters have been packed into each of the texture channels. In this case alphaChnl describes what is stored in each channel.
    alphaChnl	Set to 0 if the channel holds the glyph data, 1 if it holds the outline, 2 if it holds the glyph and the outline, 3 if its set to zero, and 4 if its set to one.
    redChnl	    Set to 0 if the channel holds the glyph data, 1 if it holds the outline, 2 if it holds the glyph and the outline, 3 if its set to zero, and 4 if its set to one.
    greenChnl	Set to 0 if the channel holds the glyph data, 1 if it holds the outline, 2 if it holds the glyph and the outline, 3 if its set to zero, and 4 if its set to one.
    blueChnl	Set to 0 if the channel holds the glyph data, 1 if it holds the outline, 2 if it holds the glyph and the outline, 3 if its set to zero, and 4 if its set to one.
    """

    def __init__(self):
        self.line_height = 0
        self.base = 0
        self.scale_w = 0
        self.scale_h = 0
        self.pages = 1
        self.packed = 1
        self.alpha_chnl = 0
        self.red_chnl = 4
        self.green_chnl = 4
        self.blue_chnl = 4

    def text(self):
        return "common lineHeight=%s base=%s scaleW=%s scaleH=%s pages=%s packed=%s alphaChnl=%s redChnl=%s greenChnl=%s blueChnl=%s" % (
            self.line_height, self.base, self.scale_w, self.scale_h,
            self.pages, self.packed, self.alpha_chnl, self.red_chnl,
            self.green_chnl, self.blue_chnl
        )


class FntPage:
    """
    tag: page

    This tag gives the name of a texture file. There is one for each page in the font.

    id	    The page id.
    file	The texture file name.
    """

    def __init__(self):
        self.id = 0
        self.file = "temp.png"

    def set_file(self, file):
        self.file = os.path.splitext(os.path.basename(file))[0] + ".png"

    def text(self):
        return "page id=%s file=\"%s\"" % (self.id, self.file)


class FntChars:
    def __init__(self):
        self.count = 0

    def text(self):
        return "chars count=%s" % self.count


class FntChar:
    """
    tag: char

    This tag describes on character in the font. There is one for each included character in the font.

    id	        The character id.
    x	        The left position of the character image in the texture.
    y	        The top position of the character image in the texture.
    width	    The width of the character image in the texture.
    height	    The height of the character image in the texture.
    xoffset	    How much the current position should be offset when copying the image from the texture to the screen.
    yoffset	    How much the current position should be offset when copying the image from the texture to the screen.
    xadvance	How much the current position should be advanced after drawing the character.
    page	    The texture page where the character image is found.
    chnl	    The texture channel where the character image is found (1 = blue, 2 = green, 4 = red, 8 = alpha, 15 = all channels).
    """

    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.xoffset = 0
        self.yoffset = 0
        self.xadvance = 0
        self.page = 0
        self.chnl = 0

    def text(self):
        return "char id=%d x=%d y=%d width=%d height=%d xoffset=%d yoffset=%d xadvance=%d page=%d chnl=%d" % (
            self.id, self.x, self.y, self.width, self.height,
            self.xoffset, self.yoffset, self.xadvance,
            self.page, self.chnl
        )


class FntWriter:
    def __init__(self):
        self.__info = FntInfo()
        self.__common = FntCommon()
        self.__page = FntPage()
        self.__chars = FntChars()
        self.__characters = []

    def set_font(self, font="", size=32, bold=0, italic=0):
        self.__info.font = font
        self.__info.size = size
        self.__info.bold = bold
        self.__info.italic = italic

    def set_count(self, count):
        self.__chars.count = count

    def set_size(self, width, height, line_height):
        self.__common.scale_h = height
        self.__common.scale_w = width
        self.__common.line_height = line_height

    def add_char(self, char):
        self.__characters.append(char)

    def save(self, filename):
        self.__page.set_file(filename)
        text = []
        text.append(self.__info.text())
        text.append(self.__common.text())
        text.append(self.__page.text())
        text.append(self.__chars.text())
        text = text + self.__characters
        text = [line + "\n" for line in text]
        with open(filename, "wt") as f:
            f.writelines(text)


class Alignment(Enum):
    Center = 0
    Top = 1
    Bottom = 2


class BMFontGenerator:
    def __init__(self, where, filename="temp", max_width=1024, alignment=Alignment.Center):
        if not os.path.isdir(where):
            print("无效的图片字路径: %s" % where)
            sys.exit(-1)

        os.makedirs("./output", exist_ok=True)

        self.__alignment = alignment
        self.__max_width = min(2048, max_width)
        self.__filename = "./output/%s.png" % filename
        self.__fntname = "./output/%s.fnt" % filename
        self.__where = where
        self.__textures = []
        self.__width = 0
        self.__height = 0
        self.__total_width = 0
        self.__lines = 1
        self.__read_textures(where)
        self.__parse_textures()
        self.__merge_textures()

    def __read_textures(self, where):
        for root, _, files in os.walk(where):
            for file in files:
                if os.path.splitext(file)[-1] == ".png":
                    full = os.path.join(root, file)
                    image = Image.open(full)
                    self.__textures.append((full, image))
        if len(self.__textures) == 0:
            print("无效的图片字路径: %s" % self.__where)
            sys.exit(-1)

    def __parse_textures(self):
        self.__textures_in_line = []
        self.__lines = 1
        for path, image in self.__textures:
            self.__width = max(self.__width, image.width)
            self.__height = max(self.__height, image.height)
            self.__total_width += image.width
            if self.__total_width > self.__max_width:
                self.__total_width = image.width
                self.__lines += 1
            if len(self.__textures_in_line) < self.__lines:
                self.__textures_in_line.append([])
            self.__textures_in_line[self.__lines - 1].append((path, image))
        self.__height *= self.__lines
        self.__width = self.__lines > 1 and self.__max_width or self.__total_width

    def __merge_textures(self):
        one_height = int(self.__height / self.__lines)
        writer = FntWriter()
        writer.set_font(size=one_height)
        writer.set_count(len(self.__textures))
        writer.set_size(self.__width, self.__height, one_height)

        size = (self.__width, self.__height)
        channel = (255, 255, 255, 0)
        merge = Image.new("RGBA", size, channel)
        x = 0
        y = 0
        for i, line in enumerate(self.__textures_in_line):
            for _, v in enumerate(line):
                y = int(i * one_height)
                (path, image) = v
                img = image.crop((0, 0, image.width, image.height))
                if x + img.width > self.__max_width:
                    x = 0
                region = (x, y, image.width + x, y + image.height)
                merge.paste(img, region)
                base = os.path.splitext(os.path.basename(path))[0]
                code = base
                if len(base) > 1:
                    val = SPECIAL_CHARACTERS.get(base)
                    if val:
                        code = val
                try:
                    char = FntChar()
                    char.id = ord(code)
                    char.width = image.width
                    char.height = image.height
                    char.x = x
                    char.y = y
                    char.xoffset = 0
                    alignment = self.__alignment
                    if code in TOP_ALIGNMENT_SYMBOL:
                        alignment = Alignment.Top
                    elif code in BOTTOM_ALIGNMENT_SYMBOL:
                        alignment = Alignment.Bottom
                    if alignment == Alignment.Center:
                        char.yoffset = int((one_height - image.height) / 2)
                    elif alignment == Alignment.Top:
                        char.yoffset = 0
                    else:
                        char.yoffset = int((one_height - image.height))
                    char.xadvance = char.width
                    char.chnl = 15
                    writer.add_char(char.text())
                    x += img.width
                    print("正在添加字符: %s => %s" % (code, char.id))
                except Exception:
                    print("无效的字符: %s" % base)
        merge.save(self.__filename)
        writer.save(self.__fntname)
        print("BMFont已生成: %s" % self.__fntname)


if __name__ == '__main__':
    l = len(sys.argv)
    if l == 3:
        root = sys.argv[1]
        output = sys.argv[2]
        if root == "-h":
            show_help()
        else:
            BMFontGenerator(root, output)
    else:
        show_help()
