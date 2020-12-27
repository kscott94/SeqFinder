#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('start', type=int)
parser.add_argument('end', type=int)
parser.add_argument('--name', type=str, default='chromosome1')
parser.add_argument('--size', type=int, default=100)
parser.add_argument('--step', type=int, default=100)
args = parser.parse_args()

s = args.start
e = args.end

while s < e:
    print('%s\t%i\t%i' % (args.name, s, s + args.size))
    s = s + args.step
