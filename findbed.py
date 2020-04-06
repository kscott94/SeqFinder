#!/usr/bin/env python3

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('g', type=str)    #path/genome.fa (with fasta header)
parser.add_argument('b', type=str)    #path/bed.tab
parser.add_argument('-t','--tabular', action="store_true", help="output in tab separated format. default is fasta output")

args = parser.parse_args()

with open(args.g, 'r') as genome:

    """remove fasta header"""
    genome_sequence_initial = genome.readlines()[1:]
    genome_sequence = ''.join(genome_sequence_initial)

    """open and parse bed file"""
    with open(args.b, "r") as txt:
        bed = csv.reader(txt, delimiter="\t")
        for row in bed:
            chrom, pos_start, pos_stop = row
            pos_start = int(pos_start)
            pos_stop = int(pos_stop)

            """correct for 0-based indexing"""
            pos_start += - 1
            
            """print sequence in fasta format"""
            sequence_subset = genome_sequence[pos_start:pos_stop]
            if args.tabular:
                print('%i\t%i\t%s' % (pos_start, pos_stop, sequence_subset))  # Tab sep
            else:
                print('>%s positions %s-%s\n%s' % (chrom, pos_start, pos_stop, sequence_subset))  # fasta format