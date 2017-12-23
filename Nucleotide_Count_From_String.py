my_string = input("Enter String: ")
A = 0
T = 0
C = 0
G = 0
for i in my_string:
    if i is "A":
        A += 1
    elif i is "T":
        T += 1
    elif i is "C":
        C += 1
    elif i is "G":
        G += 1

print(str(A) + " " + str(C) + " " + str(G) + " " + str(T))
