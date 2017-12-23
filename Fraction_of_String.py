#problem 3 biot e-100
#find a slice of a string

in_string = input("Enter your string: ")
#first start point
a = int(input("a = "))
#first end point
b = int(input("b = "))
#second start point
c = int(input("c = "))
#second end point
d = int(input("d = "))

print(in_string[a:b+1] + ' ' + in_string[c:d+1])
