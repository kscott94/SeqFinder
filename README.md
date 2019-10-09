# SeqFinder

### SeqFinder is a unix-based commandline tool for finding genomics sequences from an input positoin. Note: this only works with single chromosomed organisms. Otherwise, split chromosomes into separate files. 

### The index file should contain a list of genomic positions separated by new lines

## Find: find.py
define a start and stop positon and return the corresponding sequence.
python3 find.py <path/to/genome.txt> <start> <stop>
  
example: python3 find.py ./SeqFinder/genomic_sequence.txt 1 100
returns the sequence from position 1 to 100


## Adjacent: adjacent.py
define a sing position and return a specified amount of bases before and after that position.

python3 adjacent.py -g <path/to/genome.txt> -i <path/to/index.txt> -b <positions back -f <positions forward>

example: python3 adjacent.py -g ./SeqFinder/genomic_sequence.txt -i ./SeqFinder/index.py -b 10 -f 5
returns sequences surrounding positions in index file (positions separated by lines)
