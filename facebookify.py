#!/usr/bin/env python3
import argparse
from PIL import Image, ImageFilter
import tempfile
import io

parser = argparse.ArgumentParser(description="Makes a image look like it does on facebook")
parser.add_argument('input', metavar='INPUT', help="input image")
parser.add_argument('output', metavar='OUTPUT', help="output image")
parser.add_argument('--iterations', '-i', metavar='ITERATIONS', type=int, default=256, help="how many iterations to run")
parser.add_argument('--quality', '-q', metavar='QUALITY', type=int, default=10, help="default quality")
args = parser.parse_args()

im = Image.open(args.input)
#temp = tempfile.TemporaryFile()
temp = io.BytesIO()

for i in range(args.iterations):
    for i in range(5):
        im = im.filter(ImageFilter.SHARPEN)
    im.save(temp, "JPEG", quality=args.quality)
    im = Image.open(temp)

im.save(args.output)
