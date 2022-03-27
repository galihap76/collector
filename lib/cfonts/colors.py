"""
Utility functions for handling terminal colors
"""
import os
from typing import Iterable, List, Mapping, NamedTuple, Tuple, no_type_check

import colorama

from .consts import ANSI_COLORS, ANSI_RGB


class Style(NamedTuple):
    open: str
    close: str


_Rgb = Tuple[int, int, int]
_Hsv = Tuple[float, float, float]


def support_truecolor() -> bool:
    return os.name != "nt" or (
        os.getenv("ANSICON") is not None
        or os.getenv("WT_SESSION") is not None
        or "ON" == os.getenv("ConEmuANSI")
        or "xterm" == os.getenv("Term")
    )


def hex_to_rgb(hex_string: str) -> _Rgb:
    """Return a tuple of red, green and blue components for the color
    given as #rrggbb.
    """
    assert len(hex_string) in (4, 7), "Hex color format is not correct."
    if len(hex_string) == 4:
        return tuple(int(c * 2, 16) for c in hex_string[1:])  # type: ignore
    return tuple(
        int(hex_string[i : i + 2], 16) for i in range(1, len(hex_string), 2)
    )  # type: ignore


def rgb_to_hex(rgb: _Rgb) -> str:
    return "#" + "".join("%02x" % c for c in rgb)


@no_type_check
def rgb_to_hsv(rgb: _Rgb) -> _Hsv:
    r, g, b = rgb
    r /= 255
    g /= 255
    b /= 255

    max_value = max(r, g, b)
    min_value = min(r, g, b)
    diff = max_value - min_value

    h, s, v = 0, diff / max_value if max_value > 0 else 0, max_value

    if max_value == min_value:
        h = 0
    elif max_value == r:
        h = 60 * (g - b) / diff
        if g < b:
            h += 360
    elif max_value == g:
        h = 60 * (b - r) / diff + 120
    else:
        h = 60 * (r - g) / diff + 240

    return h, (s * 100), (v * 100)


def hsv_to_rgb(hsv: _Hsv) -> _Rgb:
    h, s, v = hsv
    h /= 60
    s /= 100
    v /= 100
    hi = int(h) % 6

    f = h - int(h)
    p = 255 * v * (1 - s)
    q = 255 * v * (1 - (s * f))
    t = 255 * v * (1 - (s * (1 - f)))
    v *= 255

    result = {
        0: (v, t, p),
        1: (q, v, p),
        2: (p, v, t),
        3: (p, q, v),
        4: (t, p, v),
        5: (v, p, q),
    }[hi]
    r, g, b = result
    return int(r), int(g), int(b)


def _color_distance(left: _Hsv, right: _Hsv) -> float:
    return sum((i - j) ** 2 for i, j in zip(left, right))


def _ensure_rgb(color: str) -> _Rgb:
    if color in ANSI_RGB:
        return ANSI_RGB[color]
    return hex_to_rgb(color)


def get_closest(rgb: _Rgb, rgb_map: Mapping[str, _Rgb] = ANSI_RGB) -> str:
    """Return the closest ANSI color name from the given RGB."""
    return min(rgb_map, key=lambda name: _color_distance(rgb, rgb_map[name]))


def get_linear(start: float, end: float, steps: int) -> List[float]:
    """Get a list of numbers interpolated from start to end inclusively."""
    step = (end - start) / (steps - 1)
    return [start + i * step for i in range(steps)]


def get_interpolated_hsv(
    start_hsv: _Hsv, end_hsv: _Hsv, steps: int, transition: bool = False
) -> Iterable[_Hsv]:
    """Get a sequence of HSV colors interpolated from start to end"""
    if transition:
        return zip(
            *[get_linear(s, e, steps) for s, e in zip(start_hsv, end_hsv)]
        )  # type: ignore
    s_sequence = get_linear(start_hsv[1], end_hsv[1], steps)
    v_sequence = get_linear(start_hsv[2], end_hsv[2], steps)
    start_h, end_h = start_hsv[0], end_hsv[0]
    diff = end_h - start_h
    if diff < 0:
        delta = diff if diff <= -180 else 360 + diff
    else:
        delta = diff if diff >= 180 else diff - 360
    delta = delta / (steps - 1)
    h_sequence = [(start_h + i * delta) % 360 for i in range(steps)]
    return zip(h_sequence, s_sequence, v_sequence)


class AnsiPen:
    """Generate ANSI color styles"""

    CLOSE_BIT = "\x1b[39m"
    BG_CLOSE_BIT = "\x1b[49m"

    def style(self, color: str, background: bool = False) -> Style:
        if color == "system":
            return Style("", "")
        if color in ANSI_COLORS:
            return self.ansi_style(color, background)
        elif color.startswith("#"):
            return self.hex_style(color, background)
        raise ValueError("Unsupported color: {}".format(color))

    def ansi_style(self, color: str, background: bool) -> Style:
        offset = 10 if background else 0
        close = self.BG_CLOSE_BIT if background else self.CLOSE_BIT
        code = ANSI_COLORS[color]
        return Style("\x1b[{}m".format(offset + code), close)

    def hex_style(self, color: str, background: bool) -> Style:
        return self.rgb_style(hex_to_rgb(color), background)

    def rgb_style(self, color: _Rgb, background: bool) -> Style:
        ansi_color = get_closest(color)
        return self.ansi_style(ansi_color, background)

    def get_gradient(
        self, colors: List[str], steps: int, transition: bool = False
    ) -> List[Style]:
        if transition and len(colors) < 2:
            raise ValueError("Transition gradient needs at least two colors")
        elif not transition and len(colors) != 2:
            raise ValueError("Gradient needs exactly two colors")
        rgb_colors = [_ensure_rgb(color) for color in colors]
        color_steps = [(steps - 1) // (len(rgb_colors) - 1)] * (len(rgb_colors) - 1)
        if sum(color_steps) < (steps - 1):
            color_steps[-1] += 1
        assert sum(color_steps) == steps - 1
        result: List[Style] = []
        for start, end, st in zip(rgb_colors, rgb_colors[1:], color_steps):
            start_hsv, end_hsv = rgb_to_hsv(start), rgb_to_hsv(end)
            styles = [
                hsv_to_rgb(hsv)
                for hsv in get_interpolated_hsv(start_hsv, end_hsv, st + 1, transition)
            ]
            assert len(styles) == st + 1
            if result:
                styles.pop(0)
            result.extend(self.rgb_style(c, False) for c in styles)
            # The total length = (len(colors) - 1) * st
            # where st = (steps - 1) / (len(colors) - 1)
        return result


class TrueColorPen(AnsiPen):
    def rgb_style(self, color: _Rgb, background: bool) -> Style:
        open_bit = 48 if background else 38
        close = self.BG_CLOSE_BIT if background else self.CLOSE_BIT
        r, g, b = color
        return Style("\x1b[{};2;{};{};{}m".format(open_bit, r, g, b), close)


if (os.getenv("DISABLE_TRUECOLOR") or not support_truecolor()) and not os.getenv(
    "ENABLE_TRUECOLOR"
):
    # Disable truecolor for windows
    pen = AnsiPen()
    colorama.init()
else:
    pen = TrueColorPen()
