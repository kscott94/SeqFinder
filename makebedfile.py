#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('start', type=int)
parser.add_argument('end', type=int)
parser.add_argument('--name', type=str, default='chr')
parser.add_argument('--size', type=int, default=100)
parser.add_argument('--step', type=int, default=100)
args = parser.parse_args()

c = args.start

while c < args.end:
    print('%s\t%i\t%i' % (args.name, c, c + args.size))
    c = c + args.step
