#!/env/bin/python3

'''
http://rosalind.info/problems/ba1d/
Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.
Return: All starting positions in Genome where Pattern appears as a substring. 
Use 0-based indexing.
'''
from Bio import SeqIO

def pattern_matching(pattern, seq):
    matching = [] 
    for i in range(len(seq)-len(pattern)+1): # the position where k-mer begins
        if seq[i:i+len(pattern)] == pattern:
            matching.append(i)
    return matching

print(pattern_matching('ATAT', 'GATATATGCATATACTT'))