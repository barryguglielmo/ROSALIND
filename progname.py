program_to_run = int(input("Enter 7 to run script from problem 7 and Enter 8 to run the script for problem 8: "))

if program_to_run == 7:
    nuc = "ACGT"
    for i in nuc:
        for j in nuc:
            for k in nuc:
                print (i+j+k)
                
if program_to_run == 8:
    def myFunction(n):
        print ("calling myFunction with", n)
        if (n == 1):
            return 1
        elif (n == 2):
            return 1
        else:
            return myFunction(n-1) + myFunction(n-2)

    x = myFunction(10)
    print ("Answer:", x)
else:
    print("Program Ended")
