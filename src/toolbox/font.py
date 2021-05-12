from enum import Enum

from src.toolbox.atlas import Atlas
from src.toolbox.otf import OTF
from src.toolbox.ttf import TTF


class FontMode(Enum):
    Atlas = 0
    Ttf = 1
    Otf = 2


class FontFactory:
    @staticmethod
    def run_with(mode=FontMode.Atlas, configuration=None):
        print(mode, configuration)
        if mode == FontMode.Atlas:
            Atlas(configuration).generate()
        elif mode == FontMode.Ttf:
            TTF(configuration).generate()
        elif mode == FontMode.Otf:
            OTF(configuration).generate()
