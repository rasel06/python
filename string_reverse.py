input_string = input("Enter Any String = ")
j = len(input_string)
print("Reverse Val = ")
for i in input_string:
    print(input_string[j-1],end=" ")
    j-=1
