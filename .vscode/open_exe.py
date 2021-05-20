import os


print("Press 1 to Open Calculatr")
print("Press 2 to Open Paint")
program = int(input())


if(program==1):
    os.startfile("C:\Windows\System32\calc.exe")
elif(program==2):
    os.startfile("C:\Windows\System32\mspaint.exe")

