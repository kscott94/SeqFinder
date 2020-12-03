import pandas as pd

# input:
path_to_genome = './data/TS559_genome.fa'
kmer_length = 6

#code:
kmer_list = []

with open(path_to_genome, 'r') as genome:
     """remove fasta header"""
     genome_sequence_initial = genome.readlines()[1:]
     genome_sequence = ''.join(genome_sequence_initial).replace("\n","")
     pos1 = 0
     pos2 = kmer_length
     for pos in genome_sequence:
          kmer_list.append(genome_sequence[pos1:pos2])
          pos1 += 1
          pos2 += 1

kmer_list = kmer_list[0:-5]

def reverse_compliment(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence_rc = ''.join([complement[nucleotide] for nucleotide in sequence[::-1]])
    return(sequence_rc)

kmer_list_rc = []

for kmer in kmer_list:
    rc = reverse_compliment(kmer)
    kmer_list_rc.append(rc)

palindrome_check = []

#kmer_list[0] = "AAGCTT"
#kmer_list_rc[0]="AAGCTT"

for iter in range(len(kmer_list)):
    if kmer_list[iter] == kmer_list_rc[iter]:
        palindrome_check.append("True")
    else:
        palindrome_check.append("False")

zip_list = list(zip(kmer_list,kmer_list_rc,palindrome_check))

df = pd.DataFrame(zip_list, columns=['kmer', 'rc', 'check'])
df = df[df["check"] == "True"]

print(df.kmer.value_counts())

