import os

from PySide6.QtCore import Qt, QByteArray, QBuffer
from PySide6.QtGui import QPixmap, QImage

def Base64ToBytes(filename):
    image = QImage(filename)
    ba = QByteArray()
    buff = QBuffer(ba)
    image.save(buff, "PNG")
    return ba.toBase64().data()

def isImage(filename):
 	ext = [".png", ".svg", ".jpg", ".jpeg", ".ico"]
 	return os.path.splitext(filename)[-1].lower() in ext

if __name__ == "__main__":
	data = {}
	start_path = os.path.abspath("./src/static")
	for root, dirs, files in os.walk(start_path):
		for filename in files:
			if isImage(filename):
				filepath = os.path.join(root, filename)
				base64 = Base64ToBytes(filepath)
				data[filename.replace(r".", "_")] = base64
				print(filename)
	with open("./src/helper/resources.py", "wt") as f:
		f.write("""from PySide6.QtCore import QByteArray
from PySide6.QtGui import QIcon, QPixmap

class GRes:
""")
		for k, v in data.items():
			f.write("\t%s = %s\n" % (k, v))
		f.write("\n\n")
		f.write(r"""def GMakeIcon(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64))
    icon = QIcon(pixmap)
    return icon""")

