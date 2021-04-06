rows = int(input("Number of rows = "))
k = 0



for i in range(rows+1):

    for spc in range(rows):
        print(" ",end=" ")

    while k != 2*1-1:
        print("*",end =" ")
        k+=1
    
    print("\n")
