import os

from PIL import Image

from src.toolbox.characters import (ESCAPE_CHARS, TOP_ALIGNMENT_CHARS, BOTTOM_ALIGNMENT_CHARS)
from src.toolbox.definition import (FntChar, FntWriter, Alignment)
from src.helper.common import g_signal


class BMFontGenerator:
    def __init__(self, where, output, filename, atlas, max_width=1024, alignment=Alignment.Center):
        self.__alignment = alignment
        self.__max_width = min(2048, max_width)
        self.__filename = os.path.join(output, "%s.png" % filename)
        self.__fntname = os.path.join(output, "%s.fnt" % filename)
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
        for i, line in enumerate(self.__textures_in_line):
            for _, v in enumerate(line):
                y = int(i * one_height)
                (path, image) = v
                img = image.crop((0, 0, image.width, image.height))
                if x + img.width > self.__max_width:
                    x = 0
                region = (x, y, image.width + x, y + image.height)
                base = os.path.splitext(os.path.basename(path))[0]
                code = base
                if len(base) > 1:
                    val = ESCAPE_CHARS.get(base)
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
                    if code in TOP_ALIGNMENT_CHARS:
                        alignment = Alignment.Top
                    elif code in BOTTOM_ALIGNMENT_CHARS:
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
                    merge.paste(img, region)
                    print("正在添加字符: %s => %s" % (code, char.id))
                except TypeError:
                    print("无效的字符: %s" % base)
        merge.save(self.__filename)
        writer.save(self.__fntname)
        g_signal.msgbox_trigger.emit("BMFont已生成: %s" % self.__fntname)


class Atlas:
    def __init__(self, configuration: dict):
        self.configuration = configuration

    def generate(self):
        from_dir = self.configuration.get("image")
        output_dir = self.configuration.get("output")
        atlas = self.configuration.get("atlas")
        BMFontGenerator(from_dir, output_dir, os.path.basename(from_dir), atlas, 1024, Alignment.Bottom)
