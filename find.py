#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('txt', type=str)    #path/genome.txt
parser.add_argument('start', type=int)
parser.add_argument('stop', type=int)

args = parser.parse_args()


with open(args.txt, 'r') as genome:
    pos = genome.read().replace('\n', '')
    args.start = args.start - 1
    genome_seq = pos[args.start:args.stop]
    print(genome_seq)
