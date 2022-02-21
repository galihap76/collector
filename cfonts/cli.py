"""
    Python cFonts
    =============
    Sexy fonts for the console.

    :license: GNU GPLv2
    :author: Frost Ming<mianghong@gmail.com>
"""
import argparse
import sys
from typing import List, Optional

from . import consts
from .__version__ import __version__
from .core import render, say


class CFontsArgumentParser(argparse.ArgumentParser):
    def format_help(self) -> str:
        formatter = self._get_formatter()

        # description
        formatter._add_item(
            lambda x: x,
            [render("cfonts", gradient=["red", "green"], space=False) + "\n"],
        )
        formatter.add_text(self.description)

        # usage
        formatter.add_usage(
            self.usage or "", self._actions, self._mutually_exclusive_groups
        )

        # positionals, optionals and user-defined groups
        for action_group in self._action_groups:
            formatter.start_section(action_group.title)
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        # epilog
        formatter.add_text(self.epilog)

        # determine help from format above
        return formatter.format_help()


def parse_args() -> argparse.Namespace:
    parser = CFontsArgumentParser(
        "cfonts",
        description="This is a tool for sexy fonts in the console. "
        "Give your cli some love.",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="{} {}".format(
            render("cfonts", font="console", colors=["candy"], space=False), __version__
        ),
    )

    parser.add_argument(
        "-f",
        "--font",
        default=consts.FontFaces.block.value,
        choices=[f.value for f in consts.FontFaces],
        help="Use to define the font face",
    )
    parser.add_argument(
        "-c",
        "--colors",
        default=consts.Colors.system.value,
        help="Use to define the font color",
    )
    parser.add_argument(
        "-b",
        "--background",
        default=consts.BgColors.transparent.value,
        help="Use to define the background color",
    )
    parser.add_argument(
        "-a",
        "--align",
        default="left",
        choices=consts.ALIGNMENT,
        help="Use to align the text output",
    )
    parser.add_argument(
        "-l", "--letter-spacing", type=int, help="Use to define the letter spacing"
    )
    parser.add_argument(
        "-z", "--line-height", default=1, help="Use to define the line height"
    )
    parser.add_argument(
        "-s",
        "--spaceless",
        dest="space",
        default=True,
        action="store_false",
        help="Use to define the background color",
    )

    parser.add_argument(
        "-m",
        "--max-length",
        default=0,
        help="Use to define the amount of maximum characters per line",
    )
    parser.add_argument(
        "-g",
        "--gradient",
        help="Define gradient colors(separated by comma)",
    )
    parser.add_argument(
        "-i",
        "--independent-gradient",
        action="store_true",
        help="Set this option to re-calculate the gradient colors for each new line."
        "Only works in combination with the gradient option.",
    )
    parser.add_argument(
        "-t",
        "--transition-gradient",
        dest="transition",
        action="store_true",
        help="Set this option to generate your own gradients. Each color set "
        "in the gradient option will then be transitioned to directly.",
    )
    parser.add_argument("text")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_args()

    colors = [c.strip() for c in args.colors.split(",")]
    if args.gradient:
        gradient: Optional[List[str]] = [g.strip() for g in args.gradient.split(",")]
    else:
        gradient = None
    options = {
        "font": args.font,
        "colors": colors,
        "background": args.background,
        "align": args.align,
        "line_height": args.line_height,
        "space": args.space,
        "max_length": args.max_length,
        "gradient": gradient,
        "independent_gradient": args.independent_gradient,
        "transition": args.transition,
    }
    if args.letter_spacing is not None:
        options["letter_spacing"] = args.letter_spacing
    say(args.text, **options)
