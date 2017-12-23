#problem 5 biot e-100
#print all even lines
import os
os.chdir("C:/Users/bag019/Desktop")
infile = input("Enter name of infile: ")
infile = open(infile, 'r')
outfile = open("outfile.txt", 'w')
line_number = 1
for line in infile:
    if line_number %2 == 0:
        outfile.write(line)
        line_number += 1
    else:
        line_number += 1
outfile.close()  

