from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC


dna_seq = {}
for record in SeqIO.parse("C:/Users/Barry/Desktop/FASTA.txt","fasta"):
    dna_seq[record.id] = record.seq
## Access Key and Values of Dict
x = 0
for k,v in dna_seq.items():
    if v == v.reverse_complement():
        x += 1
print (x)
