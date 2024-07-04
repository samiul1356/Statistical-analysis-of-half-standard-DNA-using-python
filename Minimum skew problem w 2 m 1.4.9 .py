# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew_raw = SkewArray(Genome)
    values_min = min(skew_raw.values())
    for key, value in skew_raw.items():
        if value == values_min:
            positions.append(key)
                
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = {} # output variable
    # your code here
    current_skew = 0
    for index, nucleotide in enumerate(Genome):
        if nucleotide == "G":
                current_skew += 1
        elif nucleotide == "C":
                current_skew -= 1
        
        skew[index+1] = current_skew
    return skew
