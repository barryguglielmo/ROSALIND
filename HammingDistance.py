##from Bio.Seq import translate
##import re
##
##coding_dna = input("Enter Coding DNA: ")
##
##for m in re.finditer("ATG",coding_dna):
##    print (m.start())
##    print(translate(coding_dna[m.start():len(coding_dna)-len(coding_dna) % 3],to_stop = True))
####translated = translate(coding_dna, stop_symbol = "")
####print (str(translated).find(str(motif)) + 1)
##
from Bio import SeqIO
from scripts import HammingDistance

# Read the input data.
with open('data/armory/rosalind_subo.txt') as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
r = 'AGTGCTTGGTCATGTCTGCCTTGGAGGTCTAGG'

# Count the number of occurences in each sequence.
count = [sum([HammingDistance(dna[seq_num][i:i+len(r)], r) <= 3 for i in xrange(len(dna[seq_num]) - len(r) + 1)]) for seq_num in xrange(2)]

# Print and save the answer.
print ' '.join(map(str, count))
with open('output/armory/Armory_014_SUBO.txt', 'w') as output_data:
    output_data.write(' '.join(map(str, count)))
