import json
import os

from helper.path import is_ext_matched, get_app_cache_dir


class Config:
    def __init__(self, filename):
        dir_name = get_app_cache_dir()
        os.makedirs(dir_name, exist_ok=True)
        config_path = os.path.join(dir_name, filename)
        self.path = config_path
        self.data = dict()
        if os.path.isfile(config_path):
            self.__load()
        else:
            self.save()

    def __load(self):
        with open(self.path, "rt", encoding="utf8") as f:
            try:
                self.data = json.loads(f.read())
            except:
                self.data = {}

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
