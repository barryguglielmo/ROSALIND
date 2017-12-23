from Bio.Seq import translate
import re

coding_dna = input("Enter Coding DNA: ")
motif = input("Enter Motif: ")
for m in re.finditer("ATG",coding_dna):
    if motif in translate(coding_dna[m.start()::],to_stop = True)
        print (m.start())
        print(translate(coding_dna[m.start()::],to_stop = True))
##translated = translate(coding_dna, stop_symbol = "")
##print (str(translated).find(str(motif)) + 1)

