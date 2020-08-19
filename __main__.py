"""
PhotoFitter
===========

This program will fit your photos into canvases for printing. This script will
take the images from the folder specified and fit them into the specified
dimensions, so that the images are as big as possible.

"""

__author__      = "Miguel Ángel Fernández Gutiérrez (@mianfg)"
__copyright__   = "Copyright 2020, @mianfg"
__credits__     = ["Miguel Ángel Fernández Gutiérrez"]
__license__     = "MIT"
__version__     = "1.0.1"
__mantainer__   = "Miguel Ángel Fernández Gutiérrez"
__email__       = "hello@mianfg.me"
__url__         = "https://go.mianfg.me/photofitter"
__status__      = "Production"



import fitter
import cli

params = cli.get_params()
if params['print_params']: print("Parameters:", params)
fitter.handle_fitter(params)
