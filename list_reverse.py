#Input like
# mango,banana,lichi,malta,grape,orrange,coconut
input_string = input("Enter enter fruits list (, seperated value)= ")

words = input_string.split(",")
#words.sort()
print("Before Reverse the list")
print("* * * * * * * * * * * *")
for index in range(len(words)):
    print(words[index])

print("* * * * * * * * * * * *")
print("After Reverse the list")
print("* * * * * * * * * * * *")
reversed(words)
for index in reversed(words):
    print(index)
