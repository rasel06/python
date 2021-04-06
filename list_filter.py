languages = ["python", "java", "dart", "php", "javascript","fortan","C#","actionscript"]
newlanguagesList = []

for item in languages:
# Filtereing the languages which name containn n
  if "n" in item:
    newlanguagesList.append(item)

print(newlanguagesList)