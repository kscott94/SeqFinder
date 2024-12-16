# SeqFinder

### SeqFinder is a set of commandline interfaced python3 scripts for finding genomic sequences at specified coordinate positions in the Thermococcus kodakarensis genome.  

Note: If the genome contains multiple chromosomes, split chromosomes into separate files. 

current version: 1.3

## Find: find.py
define a start and stop positon in the genome and return the corresponding sequence between those coordinate positions.\
python3 find.py [-options] <path/to/genome.fa> <start> <stop>\
-fa option outputs sequence in fasta format
  
example: python3 find.py genome.fa 1 100\
returns the nucleotide sequence from position 1 to 100


## FindBed: findbed.py
input a tab separated file with chromosome, start position, stop position. Put each genomic interval on a new line.\
python3 find.py [-t] genome.fasta outfile.tsv\
returns fasta file with sequences from indicated start and stop positions. \
-t option outputs sequences in tab separated format. By default, output is in fasta format.


## Adjacent: adjacent.py
define a single position and return the sequence with a specified amount of bases before and after that position.
The specified position(s) should be in a line separated file, here called index.txt. \
-t option allows output in tab separated format. By default, output is in fasta format.

python3 adjacent.py [-t] genome.fa index.txt -b < positions 5' > -f < positions 3' >

example: python3 adjacent.py genome.fa index.txt -f 10 -b 10\
returns 10 nt of up and downstream sequence surrounding each line separtaed positions specific in the index file

## Fasta pull: fasta_pull.py
required packages: biopython
Unlike the other scripts in this repository, fasta pull is NOT run from the command line. This script takes in a line separated list of *Thermoccoccus kodakarensis* gene tags, and pulls out the fasta sequence of those genes from a master fasta file that contains a full set of gene sequences. For example, I downloaded from KEGG a fasta file with every gene in fasta format from *Thermoccoccus kodakarensis*. I can provide a list of gene names and pull out the fasta sequences of those genes from the master fasta file creating a subsetted fasta sequences with only the genes of interest. 

input: line separated list of gene tags, master fasta file, and output file name. 

## Primer design: primer_design.py
Design primers for an input DNA sequence. Indicate the length of the forward and reverse primers. Optionally, specify 5' and extension sequences for your primers. Primers will be utputed in fasta format. 

python3 primer_design.py [-options] <dna_sequence>

options:\
-f: 5' extension to forward primer\
-r: 5' extension to reverse primer

example: python3 primer_design.py TGCAGCTCGGCAAACTCTTAGGCTTAGC 12 13
returns forward and reverse primer sequences of 12 and 12 bases, respectively in fasta format, against the input sequence.The fasta will also contain the estimated Tm for each primer.  

## Reverse compliment: revcomp
Reverse complimnet input sequence

## Make bed file: makebedfile.py
make an empty bed file with chrosome name, start position and stop poistion based on defined region width and step sizes.
