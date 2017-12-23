#problem 4 biot e-100
#sum of all odd integers a through b (inclusive)
a = int(input("a = "))
b = int(input("b = "))

total = 0
for i in range(a, b +1):
    if i % 2 == 1:
        total += i
print(total)
