from Bio import SeqIO

list_of_genes = "./TS559_m5c_transcripts"
fasta_file = "./data/tk_genes.fa"

fasta_dict = {rec.id : rec.seq for rec in SeqIO.parse(fasta_file, "fasta")}
subset_dict = {}

with open(list_of_genes,"r") as genes:  # Pull fasta sequence of genes from master file
    for gene in genes:
        gene=gene.strip()
        gene_sequence = str(fasta_dict[gene]).upper().replace("T", "U") # Direct conversion of DNA coding sequence to RNA
        subset_dict.update({gene : gene_sequence})

with open("./data/fasta_subset.fa", "a") as subsetted_fasta:    # Creat fasta file of subsetted dictionary
    for key in subset_dict:
        subsetted_fasta.write(">%s\n" % key)
        subsetted_fasta.write(subset_dict[key])
        subsetted_fasta.write("\n")
