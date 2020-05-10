#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('genome', type=str, help="First argument is the path to genome sequence in fasta format")
parser.add_argument('index', type=str, help = "Second argument is the path to index file containing genomic positions separated by newlines")
parser.add_argument('-b', type=int, help="Number of nucleotides to display behind (5' of) position specified in -i file")
parser.add_argument('-f', type=int, help="Number of nucleotides to display in-front of (3' of) position specified in -i file")
parser.add_argument('-t','--tabular', action="store_true", help="output in tab seperated format")

args = parser.parse_args()

with open(args.genome, 'r') as genome:
    """remove fasta header"""
    genome_sequence_initial = genome.readlines()[1:]
    genome_sequence = ''.join(genome_sequence_initial).replace("\n","")

    """open and parse index file"""
    with open(args.index, 'r') as index_positions:
        mC_pos = index_positions.readlines()
        for line in mC_pos:
            line = int(line)
            position = line - 1
            backwords = position - args.b  #5' of position
            forwords = position + 1 + args.f  # 3' of position; correct for 0-based indexing

            """create and print sequence object"""
            sequence_subset = genome_sequence[backwords:forwords]
            if args.tabular:
                print('%i\t%s' % (line, sequence_subset))  # Tab separated
            else:
                print('>%i\n%s' % (line, sequence_subset))  # fasta format
