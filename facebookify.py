#!/usr/bin/env python3
import argparse
from PIL import Image
import tempfile

parser = argparse.ArgumentParser(description="!@#")
parser.add_argument('input', metavar='INPUT', help="input image")
parser.add_argument('output', metavar='OUTPUT', help="output image")
parser.add_argument('--iterations', '-i', metavar='ITERATIONS', type=int, default=1024, help="how many iterations to run")
parser.add_argument('--quality', '-q', metavar='QUALITY', type=int, default=1, help="default quality")
args = parser.parse_args()

im = Image.open(args.input)
temp = tempfile.TemporaryFile()

for i in range(args.iterations):
    im.save(temp, "JPEG", quality=args.quality)
    im = Image.open(temp)

im.save(args.output)
