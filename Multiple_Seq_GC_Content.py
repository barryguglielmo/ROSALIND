#problem 9 biot e-100
#FASTA using biopython
from Bio import SeqIO
#path
import os
os.chdir("C:/Users/bag019/Desktop")
infile = input("Enter infile: ")
#3d array of the fasta
dna_seq = [[],[],[]]
#biopython read in data
for record in SeqIO.parse(infile,"fasta"):
    dna_seq[0].append(record.id)
    dna_seq[1].append(record.seq)
#get the gc contents
for i in range(0, len(dna_seq[1])):
    GC = 0
    total = 0
    for letter in dna_seq[1][i]:
        if letter == 'G' or letter =='C':
            GC+= 1
            total += 1
        else:
            total += 1
    dna_seq[2].append((GC/total)*100)
#get the highest gc index and then print the corrosponding ID then the GC content
print(dna_seq[0][dna_seq[2].index(max(dna_seq[2]))])
print(max(dna_seq[2]))
