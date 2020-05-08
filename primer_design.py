#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('seq', type=str, help="sequence 5' to 3' to create primers against")
parser.add_argument('length_F', type=int, help="length of forward primer")
parser.add_argument('length_R', type=int, help="length of reverse primer")
parser.add_argument('-f',default="", type=str, help="5' to 3' sequence to add to 5' end of Forward primer")
parser.add_argument('-r',default="", type=str, help="5' to 3' sequence to add to 5' end of Reverse primer")

args = parser.parse_args()

def RC(seq):
    seq = seq.upper()
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

def rc(seq):
    complement = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))
    return reverse_complement

primer_F = args.f.lower() + args.seq[0:args.length_F].upper()
primer_R = rc(args.r).lower() + RC(args.seq[ len(args.seq)-args.length_R: ] ).upper()


F_Tm = 0
for base in primer_F:
    F_Tm = F_Tm + 2

R_Tm = 0
for base in primer_R:
    R_Tm += 2

print(">primer_F Tm: %s" % F_Tm)
print(primer_F)

print(">primer_R Tm: %s" % R_Tm)
print(primer_R)