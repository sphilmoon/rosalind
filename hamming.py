# reference: https://rosalind.info/problems/hamm/

def hamming_distance(s, t):
    # Initialize the counter for Hamming distance
    distance = 0
    
    # Loop through both strings simultaneously using zip()
    for nucleotide_s, nucleotide_t in zip(s, t):
        # Compare nucleotides at the same position
        if nucleotide_s != nucleotide_t:
            distance += 1
    
    # Return the Hamming distance
    return distance

# Sample input
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

# Call the function and print the result
print(hamming_distance(s, t))