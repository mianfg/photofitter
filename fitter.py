"""
fitter
======

Image rendering facilities

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



from PIL import Image, ImageDraw
from os import walk, path, makedirs
import re
from progress.bar import Bar


def fit(img, base, size, offset):
    w, h = img.size

    # check orientation, match orientation of base by rotating
    if (w > h and size[0] < size[1]) or (w < h and size[0] > size[1]):
        img = img.transpose(Image.ROTATE_90)
    
    # resize so that it fits size:
    w, h = img.size
    # resize in width
    w, h = size[0], size[0]*h/w
    # resize in height if it surpasses height
    if h > size[1]:
        w, h = w*size[1]/h, size[1]
    w, h = int(w), int(h)
    img = img.resize((w,h))

    base.paste(img, offset)


def process_subdivisions(paths, canvas, subdivisions, lines, background_color, line_color, line_thickness, output):
    base = Image.new('RGB', canvas, background_color)

    if lines:
        d = ImageDraw.Draw(base)
        for i in range(subdivisions[0]):
            location = [((i+1)*canvas[0]/subdivisions[0], 0), ((i+1)*canvas[0]/subdivisions[0], canvas[1])]
            d.line(location, fill=line_color, width=line_thickness)
        for i in range(subdivisions[1]):
            location = [(0,(i+1)*canvas[1]/subdivisions[1]), (canvas[0], (i+1)*canvas[1]/subdivisions[1])]
            d.line(location, fill=line_color, width=line_thickness)

    n = 0
    v = 0
    for path in paths:
        img = Image.open(path)
        offset = (n%subdivisions[0],v)
        offset = (int(offset[0]*canvas[0]/subdivisions[0]), int(offset[1]*canvas[1]/subdivisions[1]))
        fit(img, base, (canvas[0]/subdivisions[0], canvas[1]/subdivisions[1]), offset)
        n += 1
        if n % subdivisions[0] == 0: v += 1

    base.save(output)


def handle_fitter(params):
    files = []
    for root, _, filenames in walk(params['folder']):
        for filename in filenames:
            if not filename.endswith(".py") and bool(re.match(params['regex'], filename)):
                files.append(path.join(root, filename))
        if not params['recursive']: break

    if not path.exists(params['output']):
        makedirs(params['output'])

    canvas = (params['dimensions'][0]*params['pixels'], params['dimensions'][1]*params['pixels'])

    items = params['subdivisions'][0]*params['subdivisions'][1]
    files_split = [files[i:i + items] for i in range(0, len(files), items)]

    n = params['startfrom']
    bar = Bar('Rendering photos', max=len(files_split))
    for chunk in files_split:
        process_subdivisions(chunk, canvas, params['subdivisions'], params['lines'], \
            params['background_color'], params['line_color'], params['line_thickness'], \
            path.join(params['output'], f"{params['name']}_{n}.jpg"))
        bar.next()
        n += 1

    bar.finish()

    print(f"{len(files)} photos fitted in {len(files_split)} canvases " \
        f"exported to {params['output']} from {params['folder']}")
