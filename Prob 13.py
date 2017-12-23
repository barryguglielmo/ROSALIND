from Bio import Entrez
from Bio import SeqIO

number_of_seq = input("Enter number strings: ")
string_of_seq = input("Enter sequences: ")

def shortest_seq (string_of_seq, number_of_seq):
    Entrez.email = "your_name@your_mail_server.com"
    handle = Entrez.efetch(db="nucleotide", id=[string_of_seq], rettype="fasta")
    records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
    shortest = len(records[0].seq)
    seq_id = 0
    for i in range (1, number_of_seq):
        if len(records[i].seq) < shortest:
            shortest = len(records[i].seq)
            seq_id = i
    print (">" + records[seq_id].description)  #first record id
    print(records[seq_id].seq)  #length of the last record
shortest_seq(string_of_seq, int(number_of_seq))
