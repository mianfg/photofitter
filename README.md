<p align="center">
    <a href="https://mianfg.me"><img src="https://mianfg.me/static/img/logos/photofitter.png" alt="PhotoFitter" width="300px"></a>
</p>

<h1 align="center"><p align="center">PhotoFitter</h1></h1>
<p align="center" id="badges">
    <a href="https://github.com/mianfg/photofitter/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mianfg/photofitter" alt="License"></a> <a href="#"><img src="https://img.shields.io/github/languages/code-size/mianfg/photofitter" alt="Code size"></a> <a href="https://github.com/mianfg/photofitter/commits"><img src="https://img.shields.io/github/last-commit/mianfg/photofitter" alt="Last commit"></a> <a href="#"><img src="https://img.shields.io/badge/status-production-green" alt="More info"></a> <a href="https://go.mianfg.me/photofitter"><img src="https://img.shields.io/badge/-more%20info-orange" alt="More info"></a>
</p>

> Created by **Miguel Ángel Fernández Gutiérrez** (<https://mianfg.me/>)

A CLI app to fit your photos into canvases for printing.

## Installation

You can install PhotoFitter using `pip` or manually, if you prefer.

### Using `pip`

Simply request `pip` to install `photofitter`.

```bash
$ pip install photofitter
```

### Manual

Clone PhotoFitter's repo and run the code.

```bash
$ git clone https://github.com/mianfg/photofitter
$ cd photofitter
$ python setup.py install
```

## Usage

PhotoFitter includes a help command, simply type:

```bash
$ photofitter -h
```

You will get the full list of commands, as so:

```
usage: photofitter [-h] [-V] [-d DIMENSIONS] [-s SUBDIVISIONS] [-p PIXELS]
                   [-f FOLDER] [-l] [-B BACKGROUND_COLOR] [-L LINE_COLOR]
                   [-T LINE_THICKNESS] [-R] [-o OUTPUT] [-n NAME]
                   [-t STARTFROM] [-r REGEX] [-P]

This program will fit your photos into canvases for printing, and then
cutting. This script will take the images from the folder specified and fit
them into the specified dimensions, so that the images are as big as possible.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program version
  -d DIMENSIONS, --dimensions DIMENSIONS
                        dimensions of canvas to fit images, in
                        {width}x{height} mm [150x100 by default]
  -s SUBDIVISIONS, --subdivisions SUBDIVISIONS
                        subdivisions of canvas, in {columns}x{rows} [2x1 by
                        default]
  -p PIXELS, --pixels PIXELS
                        pixels for each mm [20 by default]
  -f FOLDER, --folder FOLDER
                        insert folder location [. by default]
  -l, --lines           show subdivision lines [not by default]
  -B BACKGROUND_COLOR, --background-color BACKGROUND_COLOR
                        background color of image, in HTML [ffffff by default]
  -L LINE_COLOR, --line-color LINE_COLOR
                        color of lines, in HTML [000000 by default]
  -T LINE_THICKNESS, --line-thickness LINE_THICKNESS
                        thickness of lines, in px [2 by default]
  -R, --recursive       iterate folder recursively [non-recursive search by
                        default]
  -o OUTPUT, --output OUTPUT
                        location of output folder [./output by default]
  -n NAME, --name NAME  output name prepended to every image [fitter by
                        default]
  -t STARTFROM, --startfrom STARTFROM
                        number to start output filename with [0 by default]
  -r REGEX, --regex REGEX
                        regular expression: only files matching the regular
                        expression will be parsed [.* by default]
  -P, --print-params    print parameters
```

Here are more detailed explanations on each of the commands:

| Command name | Directive | Description |
| --- | --- | --- |
| **Help** | `-h`, `--help` | Receive help about how to use PhotoFitter. Overrides all commands |
| **Version** | `-V`, `--version` | Version information |
| **Canvas dimensions** | `-d DIMENSIONS`, `--dimensions DIMENSIONS` | Dimensions, in mm, of the canvas in which the photos will be rendered. All the photos rendered will have these dimensions. `DIMENSIONS` must be in the format `{width}x{height}`. By default, dimensions are `150x100`. |
| **Subdivisions** | `-s SUBDIVISIONS`, `--subdivisions SUBDIVISIONS` | Number of subdivisions of canvas in which the photos will be fit. `SUBDIVISIONS` must be in the format `{columns}x{rows}`. By default, subdivisions are `2x1`. |
| **Resolution** | `-p PIXELS`, `--pixels PIXELS` | Specifies the image resolution, in pixels per mm. By default, resolution is `20`. |
| **Folder** | `-f FOLDER`, `--folder FOLDER` | Folder route to retrieve images. Route can be relative or absolute. By default, route is `.` |
| **Show lines** | `-l`, `--lines` | Show lines in subdivisions |
| **Background color** | `-B BACKGROUND_COLOR`, `--background-color BACKGROUND_COLOR` | Background color of canvases. `BACKGROUND_COLOR` must be a color in hex form, six characters. By default, background color is `FFFFFF`. |
| **Line color** | `-L LINE_COLOR`, `--line-color LINE_COLOR` | Line color for subdivisions (see _show lines_). `LINE_COLOR` must be a color in hex form, six characters. By default, line color is `000000`. |
| **Recursive iterating** | `-R`, `--recursive` | Iterate images in folder recursively. |
| **Output foler** | `-o OUTPUT`, `--output OUTPUT` | Route to export images, can be absolute or relative. If folder does not exist, it will be generated. |
| **Output name** | `-n NAME`, `--name NAME` | Rendered filenames will be of the format `{NAME}_{NUMBER}.jpg`. By default, output name is `fitter`. |
| **Output start number** | `-t STARTFROM`, `--startfrom STARTFROM` | Rendered filenames will be of the format `{NAME}_{NUMBER}.jpg`, with `NUMBER` being `STARTFROM` + `INDEX`, with `INDEX` being the number of picture generated, starting from 0 and incrementing by 1. By default, output start number is `0`. |
| **Regex** | `-r REGEX`, `--regex REGEX` | Only files matching the regular expression `REGEX` will be parsed. By default, regex is `.*` (all files) |
| **Print parameters** | `-P`, `--print-params` | Print dict of parameters |