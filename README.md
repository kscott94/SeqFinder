# SeqFinder

### SeqFinder is a set of miscellaneous, linux-based, commandline tool for finding genomic sequences at specified sequence positions. This tool depends on python3.

Note: if the genome contains multiple chromosomes, split chromosomes into separate files. 

current version: 1.1

## Find: find.py
define a start and stop positon and return the corresponding sequence.
python3 find.py [-options] <path/to/genome.fa> <start> <stop>
-fa option outputs sequence in fasta format
  
example: python3 find.py genome.fa 1 100
returns the sequence from position 1 to 100


## FindBed: findbed.py
input a tab separated file with chromosome, start position, stop position
python3 find.py [-options] genome.fa bed.tsv
returns fasta file with sequences from indicated start and stop positions. -t option outputs sequences in tab separated format. 


## Adjacent: adjacent.py
define a single position and return the sequence with a specified amount of bases before and after that position.
The specified position(s) should be in a line sperated file, here called index.txt. -t option allows output in tab separated format.

python3 adjacent.py [-options] genome.fa index.txt -b <positions back> -f <positions forward>

example: python3 adjacent.py genome.fa index.txt -f 10 -b 10
returns sequences surrounding positions in index file
