#!/env/bin/python3

'''
http://rosalind.info/problems/ba1b/
Find the Most Frequent Words in a String

Given: A DNA string seq and an integer k.
Return: All most frequent k-mers in seq (in any order).
'''

from Bio import SeqIO

def most_frequent_kmers(seq, k):
    count = {}
    for i in range(len(seq)-k+1):
        if seq[i:i+k] not in count:
            count[seq[i:i+k]] = 0
        else:
            count[seq[i:i+k]] += 1
    frequent = max(count.values())

    for k, v in count.items():
        if v == frequent:
            print(k, end="")
    return count

most_frequent_kmers('ACAACTATGCATCACTATCGGGAACTATCCT', 5)