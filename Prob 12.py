from Bio import Entrez
# I found this example code online *https://github.com/adelq/rosalind/commit/5472a340628dc13774a7a0b833724466914136b4
# Don't reinvent the wheel if you dont have to
# Define the function
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
