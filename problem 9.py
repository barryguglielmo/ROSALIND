#problem 9 biot e-100
#Reverse Complement
#path
import os
os.chdir("C:/Users/bag019/Desktop")
#input and outfile
my_string = input("Enter String: ")
new_string = []
#go through each letter and replace
for letter in my_string:
    if letter == 'A':
        new_string.append('T')
    elif letter == 'T':
        new_string.append('A')
    elif letter == 'G':
        new_string.append('C')
    elif letter == 'C':
        new_string.append('G')
        
#reverse it
reverse = reversed(new_string)
#join and print it
print(''.join(reverse))

