from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('Q8EKP0') #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
##print(record.organism_classification)

for i in record.cross_references:
    if (i[0] == 'GO'):
       if (i[2][0] == 'P'):
           print (i[2][2:])
