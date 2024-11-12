# reference: https://rosalind.info/problems/subs/

# Approach
# 1. Iterate thru s: loop thru the strings s and check at each position 
# if the substring t starts there.
# 2. Substring matching: at each position i, check if the substring of 
# length equal to t matches t. 
# 3. 1-based index: return the positions in 1-based index (e.g. counting 
# positions starting from 1 instead of 0.)


def find_substring_locations(s, t): 
    positions = [] # List to store the positions where t occurs within s 

    # Iterate through string s to check for occurrences of t
    for i in range(len(s) - len(t) + 1):
        # If the substring of s from i to i+len(t) matches t 
        if s[i:i+len(t)] == t:
            # Append the 1-based index (i+1) to positions
            positions.append(i + 1)

    return positions 

# Sample input 
s = "GATATATGCATATACTT"
t = "ATAT"

# Call the function and print the result
result = find_substring_locations(s ,t)
print(", ".join(map(str, result)))