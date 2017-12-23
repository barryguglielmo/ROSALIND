from Bio import Entrez
#http://biopython.org/DIST/docs/api/Bio.Entrez-module.html
d# Define the function
def genbank(genus, dtstart, dtend):
	Entrez.email = "barryguglielmo@gmai.com" 
	handle = Entrez.esearch(db="nucleotide", term='%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend))
	record = Entrez.read(handle)
	return record["Count"]
#get the input
genus = input("Enter Genus: ")
start = input("Enter Start: ")
end = input("Enter End: ")

# Tests
print (genbank(genus, start, end) )
