rows = int(input("Number of rows = "))

for i in range(rows + 1):
    k= 0
    for spc in range(rows-i):
        print(" ",end=" ")

    while k<i:
        print(" * ", end=" ")
        k+=1
    print("\n")
