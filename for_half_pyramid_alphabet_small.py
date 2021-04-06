import string

alphabets = string.ascii_lowercase

rows = int(input("Number of rows = "))

for i in range(rows+1):
    if(i>0):
        for j in range(i):
            print(alphabets[j],end =" ")
        print("\n")
