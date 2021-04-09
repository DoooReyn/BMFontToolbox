import os


def get_temp_path():
    return os.environ.get("TEMP")


def get_user_root():
    return os.environ.get("USERPROFILE")


def get_user_picture():
    return os.path.abspath(os.path.join(get_user_root(), "Pictures"))


def get_user_document():
    return os.path.abspath(os.path.join(get_user_root(), "Documents"))


def get_ext_name(path):
    return os.path.splitext(path)[-1]


def is_ext_matched(path, ext):
    return get_ext_name(path).lower() == ext.lower()


def get_image_files(path):
    files = []
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if is_ext_matched(filename, ".png"):
                files.append(filename)
    return files
