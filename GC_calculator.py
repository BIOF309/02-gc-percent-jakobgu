
# This sequence is the first 100 nucleotides of the Influenza H1N1 Virus segment 8

flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'

# Count the number of "G"s in the above sequence
G = flu_ns1_seq.count('G')

# Count the number of "C"s in the above sequence
C = flu_ns1_seq.count('C')

# Add "C" and "G" counts together
GC = C + G

# Count the total number of nucleotides in the sequence
N = len(flu_ns1_seq)

# Divide the total number of "C" and "G" nucleotides by the total number of nucleotides
GC_content = GC/N

print('relative GC content: ' + str(GC_content*100) + '%')