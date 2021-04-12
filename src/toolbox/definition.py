import os
from enum import Enum


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
        return "info face=\"%s\" size=%s bold=%s italic=%s charset=\"%s\" unicode=%s stretchH=%s smooth=%s aa=%s " \
               "padding=%s spacing=%s outline=%s" % (
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
        return "common lineHeight=%s base=%s scaleW=%s scaleH=%s pages=%s packed=%s" \
               "alphaChnl=%s redChnl=%s greenChnl=%s blueChnl=%s" % (
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
        text = [self.__info.text(), self.__common.text(), self.__page.text(), self.__chars.text()]
        text += self.__characters
        text = [line + "\n" for line in text]
        with open(filename, "wt") as f:
            f.writelines(text)


class Alignment(Enum):
    Center = 0
    Top = 1
    Bottom = 2
