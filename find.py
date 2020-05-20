#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('genome', type=str)    #path/genome.fa
parser.add_argument('start', type=int)
parser.add_argument('stop', type=int )
parser.add_argument('-fa','--fasta', action="store_true", help="output in fasta format")

args = parser.parse_args()

with open(args.genome, 'r') as genome:      # Read genome fasta file and pull out sequence of interest
    """remove fasta header"""
    genome_sequence_initial = genome.readlines()[1:]
    genome_sequence = ''.join(genome_sequence_initial).replace("\n","")

    """correct for 0 based indexing"""
    args.start += - 1

    """create and print sequence object"""
    subseted_sequence = genome_sequence[args.start:args.stop]

    if args.fasta:
        print('>positions %i-%i\n%s' % (args.start, args.stop, subseted_sequence))
    else:
        print(subseted_sequence)

