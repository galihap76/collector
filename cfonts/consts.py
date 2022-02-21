"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
import enum
from shutil import get_terminal_size
from typing import Mapping, Tuple

SIZE = get_terminal_size((80, 24))
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|!?.+-_=@#$%&()/:;,' \""


class Colors(enum.Enum):
    system = "system"
    black = "black"
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    white = "white"
    candy = "candy"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"
    bright_white = "bright_white"


class CandyColors(enum.Enum):
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    gray = "gray"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"


class BgColors(enum.Enum):
    transparent = "transparent"
    black = "black"
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"
    magenta = "magenta"
    cyan = "cyan"
    white = "white"
    bright_black = "bright_black"
    bright_red = "bright_red"
    bright_green = "bright_green"
    bright_yellow = "bright_yellow"
    bright_blue = "bright_blue"
    bright_magenta = "bright_magenta"
    bright_cyan = "bright_cyan"
    bright_white = "bright_white"


ALIGNMENT = ["left", "center", "right"]


class FontFaces(enum.Enum):
    console = "console"
    block = "block"
    simpleblock = "simpleBlock"
    simple = "simple"
    threed = "3d"
    simple3d = "simple3d"
    chrome = "chrome"
    huge = "huge"
    grid = "grid"
    pallet = "pallet"
    shade = "shade"
    slick = "slick"
    tiny = "tiny"


ANSI_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "gray": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97,
}

ANSI_RGB: Mapping[str, Tuple[int, int, int]] = {
    "black": (0, 0, 0),
    "red": (234, 50, 35),
    "green": (55, 125, 34),
    "yellow": (255, 253, 84),
    "blue": (0, 32, 245),
    "magenta": (234, 61, 247),
    "cyan": (116, 251, 253),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "bright_red": (238, 119, 109),
    "bright_green": (140, 245, 123),
    "bright_yellow": (255, 251, 127),
    "bright_blue": (105, 116, 246),
    "bright_magenta": (238, 130, 248),
    "bright_cyan": (141, 250, 253),
    "bright_white": (255, 255, 255),
}
