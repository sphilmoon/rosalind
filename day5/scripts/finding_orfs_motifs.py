from Bio import SeqIO

# Replace 'sequences.fasta' with the path to your FASTA file
for record in SeqIO.parse("sequences.fasta", "fasta"):
    print("ID:", record.id)
    print("Description:", record.description)
    print("Sequence:", record.seq)
    print("Length:", len(record.seq))

# storing the sequence information
sequences = list(SeqIO.parse("sequences.fasta", "fasta"))
print("Total Sequences:", len(sequences))


# calculating GC content 
def gc_content(sequence):
    return 100 * float(sequence.count("G") + sequence.count("C")) / len(sequence)

for record in sequences:
    print(f"GC content of {record.id}: {gc_content(record.seq):.2f}%")

# transcribing DNA to RNA
for record in sequences:
    rna_seq = record.seq.transcribe()
    print(f"RNA sequence for {record.id} is {rna_seq}")

# translating RNA to protein
for record in sequences: 
    protein_seq = record.seq.transcribe().translate() 
    print(f"Protein sequence for {record.id} is {protein_seq}")

# generating reverse complement of DNA sequence
for record in sequences:
    rev_comp = record.seq.reverse_complement()
    print(f"Reverse complement sequence for {record.id} is {rev_comp}")

# 1. finding an open reading fram (ORF)
def find_orf(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    for i in range(len(sequence) - 2):
        codon = sequence[i:i+3] # each codon consists for three-nt bases.
        if codon == start_codon:
            for j in range(i, len(sequence) - 2, 3): # in steps of three-nt
                stop_codon = sequence[j:j+3]
                if stop_codon in stop_codons:
                    orfs.append(sequence[i:j+3])
                    break
    return orfs

for record in sequences:
    orfs = find_orf(record.seq)
    print(f"ORFs for {record.id}: {[str(orf) for orf in orfs]}")

# 2. indentifying motifs in DNA seq
# motifs are specific patters in sequences that might be a binding site for
# a transcription factor (functionally crucial)
import re 

def find_motif(sequence, motif): 
	return [match.start() for match in re.finditer(motif, str(sequence))]

motif = "GCT" # for example
for record in sequences:
	positions = find_motif(record.seq, motif)
	print(f"Motif '{motif}' positions in {record.id}: {positions}")

# 3. calculating codon usage frequency 
# codon usage is important for gene expression analysis. 
from collections import Counter

def codon_usage(sequence):
	# extracting codons
	codons = [str(sequence[i:i+3]) for i in range(0, len(sequence) -2, 3)]
	codon_counts = Counter(codons)
	total_codons = sum(codon_counts.values())
	return {codon: count / total_codons for codon, count in codon_counts.items()}

for record in sequences:
	usage = codon_usage(record.seq)
	print(f"Codon usage for {record.id} is {usage}")

# customizing plots using pandas datafram and seaborn for enhancing appearnaces
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Convert dictionary to DataFrame for Seaborn
codon_df = pd.DataFrame(list(usage.items()), columns=['Codon', 'Frequency'])

# Create a Seaborn bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Codon', y='Frequency', data=codon_df, palette='viridis')
plt.xlabel("Codon")
plt.ylabel("Frequency")
plt.title("Codon Usage Frequency")
plt.xticks(rotation=90)
plt.show()
