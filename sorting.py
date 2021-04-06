#Input like
# mango,banana,lichi,malta,grape,orrange,coconut
input_string = input("Enter enter fruits list (, seperated value)= ")

words = input_string.split(",")
words.sort()

for item in reversed(words):
    print(item)