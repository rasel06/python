
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

print("\n* * * * * * * * * * * * * ")
delete_fruit = input("Which fruit you want to delete from lists ")

index = fruits_list.index(delete_fruit)
fruits_list.pop(index)

print("* * * * * * * * * * * * * \n")
#fruits_list.append(new_fruit)

print("Fruit List After Delete ")
for i in fruits_list:
    print(i)
