#problem 7 biot e-100
#path
import os
os.chdir("C:/Users/bag019/Desktop")
#input and outfile
my_string = input("Enter String: ")
outfile = open("outfile.txt", 'w')

#go through each word
for letter in my_string:
    if letter == 'T':
        outfile.write('U')
    else:
        outfile.write(letter)

#close outfile
outfile.close()

