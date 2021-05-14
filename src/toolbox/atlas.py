import os

from PIL import Image

from helper.common import Globals
from toolbox.characters import ESCAPE_CHARS, TOP_ALIGNMENT_CHARS, BOTTOM_ALIGNMENT_CHARS
from toolbox.definition import FntChar, FntWriter, Alignment
from widgets.message import Message


class BMFontGenerator:
    def __init__(self, where, output, filename, atlas, max_width=1024, alignment=Alignment.Center):
        self.__alignment = alignment
        self.__max_width = min(2048, max_width)
        self.__filename = os.path.join(output, "%s.png" % filename)
        self.__fntname = os.path.join(output, "%s.fnt" % filename)
        self.__where = where
        self.__textures = []
        self.__atlas = atlas
        self.__width = 0
        self.__height = 0
        self.__total_width = 0
        self.__lines = 1
        self.__invalid_textures = []
        if self.__check_textures():
            self.__parse_textures()
            self.__merge_textures()

    def __check_textures(self):
        for file in self.__atlas:
            base = os.path.splitext(os.path.basename(file))
            ext = base[1]
            if ext.lower() == ".png":
                image = Image.open(file)
                if image.width < self.__max_width:
                    self.__textures.append((file, image))
            else:
                self.__invalid_textures.append(file)

        if len(self.__textures) == 0:
            Message.show_error("未找到有效的图集", Globals.main_window)
            return False
        return True

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
        writer.set_size(self.__width, self.__height, one_height)

        size = (self.__width, self.__height)
        channel = (255, 255, 255, 0)
        merge = Image.new("RGBA", size, channel)
        x = 0
        count = 0
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
                    merge.paste(img, region)
                    x += img.width
                    count += 1
                    print("Atlas正在添加字符: %s => %s" % (base, char.id))
                except Exception:
                    print("无效的字符: %s" % base)
                    self.__invalid_textures.append(path)

        if count > 0:
            writer.set_count(count)
            merge.save(self.__filename)
            writer.save(self.__fntname)
            Globals.signal.open_file_trigger.emit(self.__filename)

        if len(self.__invalid_textures) > 0:
            msg = [file + "\n" for file in self.__invalid_textures]
            Message.show_warning("无效的字符：\n" + "".join(msg), Globals.main_window)


class Atlas:
    def __init__(self, configuration: dict):
        self.configuration = configuration

    def generate(self):
        from_dir = self.configuration.get("image")
        output_dir = self.configuration.get("output")
        atlas = self.configuration.get("atlas")
        max_width = self.configuration.get("max_width") or 1024
        save_file = self.configuration.get("save_file")
        BMFontGenerator(from_dir, output_dir, save_file, atlas, max_width, Alignment.Bottom)
