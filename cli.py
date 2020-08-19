"""
cli
===

Command-Line Interface parser

"""

__author__      = "Miguel Ángel Fernández Gutiérrez (@mianfg)"
__copyright__   = "Copyright 2020, @mianfg"
__credits__     = ["Miguel Ángel Fernández Gutiérrez"]
__license__     = "MIT"
__version__     = "1.0"
__mantainer__   = "Miguel Ángel Fernández Gutiérrez"
__email__       = "hello@mianfg.me"
__url__         = "https://go.mianfg.me/photofitter"
__status__      = "Production"



import argparse

parser = argparse.ArgumentParser(
    description =   "This program will fit your photos into canvases for printing, and then cutting. " \
        "This script will take the images from the folder specified and fit them into the specified dimensions, " \
        "so that the images are as big as possible.",
)
parser.add_argument(
    "-V",
    "--version",
    help="show program version",
    action="store_true"
)
parser.add_argument(
    "-d",
    "--dimensions",
    help="dimensions of canvas to fit images, in {width}x{height} mm [150x100 by default]"
)
parser.add_argument(
    "-s",
    "--subdivisions",
    help="subdivisions of canvas, in {columns}x{rows} [2x1 by default]"
)
parser.add_argument(
    "-p",
    "--pixels",
    help="pixels for each mm [20 by default]"
)
parser.add_argument(
    "-f",
    "--folder",
    help="insert folder location [. by default]"
)
parser.add_argument(
    "-l",
    "--lines",
    help="show subdivision lines [not by default]",
    action="store_true"
)
parser.add_argument(
    "-B",
    "--background-color",
    help="background color of image, in HTML [ffffff by default]"
)
parser.add_argument(
    "-L",
    "--line-color",
    help="color of lines, in HTML [000000 by default]"
)
parser.add_argument(
    "-T",
    "--line-thickness",
    help="thickness of lines, in px [2 by default]"
)
parser.add_argument(
    "-R",
    "--recursive",
    help="iterate folder recursively [non-recursive search by default]",
    action="store_true"
)
parser.add_argument(
    "-o",
    "--output",
    help="location of output folder [./output by default]"
)
parser.add_argument(
    "-n",
    "--name",
    help="output name prepended to every image [fitter by default]"
)
parser.add_argument(
    "-t",
    "--startfrom",
    help="number to start output filename with [0 by default]"
)
parser.add_argument(
    "-r",
    "--regex",
    help="regular expression: only files matching the regular expression will be parsed [.* by default]"
)
parser.add_argument(
    "-P",
    "--print-params",
    help="print parameters",
    action="store_true"
)


def hex_to_rgb(hex, default=(0,0,0)):
    h = hex.lstrip('#')
    try:
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except Exception:
        rgb = default
    return rgb


def get_params():
    args = parser.parse_args()

    if args.version:
        print(f"PhotoFitter by @mianfg v{__version__}")
        print(f"\tMore information: {__url__}")
        exit()

    dimensions = (150, 100)
    if args.dimensions:
        if len(args.dimensions.split("x")) >= 2:
            dimensions = (int(args.dimensions.split("x")[0]), int(args.dimensions.split("x")[1]))
    subdivisions = (2, 1)
    if args.subdivisions:
        if len(args.subdivisions.split("x")) >= 2:
            subdivisions = (int(args.subdivisions.split("x")[0]), int(args.subdivisions.split("x")[1]))


    return {
        'dimensions'        : dimensions,
        'subdivisions'      : subdivisions,
        'pixels'            : args.pixels if args.pixels else 20,
        'folder'            : args.folder if args.folder else ".",
        'lines'             : args.lines,
        'background_color'  : hex_to_rgb(args.background_color, (255,255,255)) if args.background_color else (255,255,255),
        'line_color'        : hex_to_rgb(args.line_color, (0,0,0)) if args.line_color else (0,0,0),
        'line_thickness'    : int(args.line_thickness) if args.line_thickness else 2,
        'recursive'         : args.recursive,
        'output'            : args.output if args.output else "./output",
        'name'              : args.name if args.name else "fitter",
        'startfrom'         : int(args.startfrom) if args.startfrom else 0,
        'regex'             : args.regex if args.regex else ".*",
        'print_params'      : args.print_params
    }