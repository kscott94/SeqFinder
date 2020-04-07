from Bio import SeqIO

list_genes = "./data/gene_list.lsv"
fasta_file = "./data/tk_genes.fa"

fasta_dict = {rec.id : rec.seq for rec in SeqIO.parse(fasta_file, "fasta")}

with open(list_genes,"r") as genes:
    genes = genes.readlines()
    for gene in genes:
        gene=gene.strip()
        gene_sequence = str(fasta_dict[gene]).upper().replace("T", "U")

        with open("./data/fasta_subset.fa", "a") as subsetted_fasta:
            subsetted_fasta.write(">%s\n" % gene)
            subsetted_fasta.write(gene_sequence)
            subsetted_fasta.write("\n")