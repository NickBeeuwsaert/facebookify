#!/usr/bin/env python3
import argparse
from PIL import Image, ImageFilter
import tempfile
import io

"""
    To be honest, I'm unsure what makes facebook images look so bad

    I initially thought it was because it was getting saved and reposted so much,
    and the JPEG compression was making it look bad.
    But I get more realistic results just running a sharpen filter on the image
    Might be a combination of both, IDK
"""

parser = argparse.ArgumentParser(description="Makes a image look like it does on facebook")
parser.add_argument('input', metavar='INPUT', help="input image")
parser.add_argument('output', metavar='OUTPUT', help="output image")
parser.add_argument('--iterations', '-i', metavar='ITERATIONS', type=int, default=5, help="how many iterations to run")
parser.add_argument('--sharpen-count', '-s', metavar='ITERATIONS', type=int, default=5, help="how many times to run a sharpen filter over the image")
parser.add_argument('--quality', '-q', metavar='QUALITY', type=int, default=10, help="default quality")
args = parser.parse_args()

im = Image.open(args.input)
temp = io.BytesIO()


for i in range(args.iterations):
    for i in range(args.sharpen_count):
        im = im.filter(ImageFilter.SHARPEN)
    im.save(temp, "JPEG", quality=args.quality)
    im = Image.open(temp)

im.save(args.output)
