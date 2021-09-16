#!/env/bin/python3

'''
http://rosalind.info/problems/ba1a/
Compute the Number of Times a Pattern Appears in a Text

Given: {DNA strings}} Text and Pattern.
Return: Count(s, p).

k-mer is a string of length k in DNA sequence that is 
overlapping to reconstruct the genome. 
'''

from Bio import SeqIO

def pattern_count(sequence, pattern):
    count = 0 
    for i in range(len(sequence)-len(pattern)+1): # the position where k-mer begins
        if sequence[i:i+len(pattern)] == pattern: # e.g. seq(4,3)
            count += 1
    return count

# pattern_count(*SeqIO.parse('data.fna', 'fasta'))
print(pattern_count("GCGCG", "GCG"))