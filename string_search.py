input_text = input("Enter any Text =")
search_text = input("You are looking for =")

no_of_word = input_text.split(" ")

if search_text in input_text:
    index = no_of_word.index(search_text)
    print(search_text, " Found @ ",index+1," no word")
else:
    print("Text Not exists")    
