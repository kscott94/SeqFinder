import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g', type=str)    #path/genome.txt
parser.add_argument('-i', type=str)    #path/index.txt
parser.add_argument('-b', type=int)    #define window backwords
parser.add_argument('-f', type=int)    #define window forwards

args = parser.parse_args()

with open(args.g, 'r') as genome:
    genome_seq = genome.read().replace('\n', '')
    with open(args.i, 'r') as index_pos:
        mC_pos = index_pos.readlines()
        for line in mC_pos:
            line = int(line)
            pos = line - 1
            backwords = pos - args.b
            forwords = pos + 1 + args.f
            logos_seq = genome_seq[backwords:forwords]
            print('%i\t%s' % (line, logos_seq))
