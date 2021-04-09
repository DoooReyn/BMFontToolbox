import json
import os

from .path import is_ext_matched, get_temp_path


class Config:
    def __init__(self, filename):
        path = os.path.join(get_temp_path(), filename)
        self.path = path
        self.data = dict()
        if os.path.isfile(path) and is_ext_matched(path, ".json"):
            self.__load()
        else:
            self.save()

    def __load(self):
        with open(self.path, "rt", encoding="utf8") as f:
            self.data = json.loads(f.read())

    def save(self):
        with open(self.path, "wt", encoding="utf8") as f:
            f.write(json.dumps(self.data, indent=2))

    def init(self, key, value):
        self.data.setdefault(key, value)

    def get(self, key):
        return self.data.get(key)

    def get_default(self, key, value):
        v = self.get(key)
        if v is None:
            return value
        return v

    def set(self, key, value):
        self.data[key] = value
