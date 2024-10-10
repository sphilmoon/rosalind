# reference: https://rosalind.info/problems/revc/

def reverse_complement(dna):
    # Create a dictionary for complements
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the DNA string using 'Slicing' 
    reversed_dna = dna[::-1]
    
    # Generate the reverse complement by replacing each nucleotide
    reverse_complement_dna = ''.join([complement[nucleotide] for nucleotide in reversed_dna])
    
    return reverse_complement_dna

# Sample input
dna = "AAAACCCGGT"

# Call the function and print the result
print(reverse_complement(dna))