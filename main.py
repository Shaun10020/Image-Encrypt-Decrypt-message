from utils.ImageFile import ImageFile
from utils.Steganography import Steganography_encode,Steganography_decode

import os
import sys
import argparse


parser = argparse.ArgumentParser(prog="Image Steganography",
                                 description="This script helps encode and decode the hidden image to the cover image using Steganography")
parser.add_argument('run',choices=['encode','decode'])
parser.add_argument('cover')
parser.add_argument('output_filename',help='Filename of the output image (in png format)')
parser.add_argument('-hidden')

args = parser.parse_args(sys.argv[1:])

if args.run == 'encode' and args.hidden:
    img1 = ImageFile(os.path.join(os.getcwd(),args.cover))
    img2 = ImageFile(os.path.join(os.getcwd(),args.hidden))
    cover = Steganography_encode(img1,img2)
    cover.saveAs(args.output_filename)
elif args.run == 'decode':
    cover = ImageFile(os.path.join(os.getcwd(),args.cover))
    hidden = Steganography_decode(cover)
    hidden.saveAs(args.output_filename)