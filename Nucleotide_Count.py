#problem 7 biot e-100
#Count Nucleotides
#path
import os
os.chdir("C:/Users/bag019/Desktop")
#input and outfile
my_string = input("Enter String: ")
outfile = open("outfile.txt", 'w')

A = 0
T = 0
C = 0
G = 0
#go through each word
for letter in my_string:
    if letter == 'A':
        A += 1
    elif letter == 'T':
        T += 1
    elif letter == 'C':
        C += 1
    elif letter == 'G':
        G += 1
#write outfile
outfile.write(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))

#close outfile
outfile.close()

