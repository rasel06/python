#Input like
# mango,banana,lichi,malta,grape,orrange,coconut

def fruits_list():
    fruits = ["mango", "banana", "lichi",
              "malta", "grape", "orrange", "coconut"]
    return fruits


fruits_list = fruits_list()
fruits_list.sort()
print("* * * * * * * * * * * * * ")
print("Current Fruit List ")
print("* * * * * * * * * * * * * ")
for i in fruits_list:
    print(i)
print("* * * * * * * * * * * * * ")
new_fruit = input("Add any fruit name not in lists ")
print("* * * * * * * * * * * * * ")
fruits_list.append(new_fruit)

print("Fruit List After Add New ")
for i in fruits_list:
    print(i)
