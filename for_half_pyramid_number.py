rows = int(input("Number of rows = "))

for i in range(rows+1):
    if(i>0):
        for j in range(i):
            print(j+1,end =" ")
        print("\n")
