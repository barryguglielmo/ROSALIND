from Bio.Seq import translate
from Bio import SeqIO
from Bio.Alphabet import IUPAC
import re
my_string = input("Enter String: ")
my_string = my_string.replace("T","U")
starts = ([m.start() for m in re.finditer('(?=AUG)', my_string)])
x=0
for item in str(starts):
    print(item)
for start in starts:
    print(translate(my_string[start::], to_stop= True))
##string = my_string.replace("T","U")
##start = string.find("AUG")
##substring = string[start::]
##
##print(substring)
##
