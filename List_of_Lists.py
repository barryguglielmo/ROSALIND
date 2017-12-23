#problem 6 biot e-100
#dictionaries
#path
import os
os.chdir("C:/Users/bag019/Desktop")
#input and outfile
my_string = input("Enter String: ")
outfile = open("outfile.txt", 'w')
#all lower
split = my_string.split()
#empty dictionary
dic = [[],[]]

#go through each word
for word in split:
    #add word to dic
    if word not in dic[0]:
        dic[0].append(word)
        dic[1].append(1)
    #if word exists += 1
    else:
        loc = dic[0].index(word)
        dic[1][loc] += 1
        
#write outfile
for i in range(0,len(dic[0])):
    outfile.write(dic[0][i] + ' ' + str(dic[1][i]) + '\n')

#close outfile
outfile.close()

