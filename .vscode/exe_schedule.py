import os
from datetime import datetime
from threading import Timer



def run_program(program):
    if(program==1):
        os.startfile("C:\Windows\System32\calc.exe")
    elif(program==2):
        os.startfile("C:\Windows\System32\mspaint.exe")


print("Press 1 to Open Calculatr")
print("Press 2 to Open Paint")
program = int(input())

now = datetime.now()
print("Current Date/Time is : ", now)

print("When do you want to run ?")

print("After Days = ")
day = int(input())

print("Hours = ")
hours = int(input())

print("Hours = ")
minutes = int(input())

x= datetime.today()


y=x.replace(day=x.day+day,hour=hours,minute=minutes,second=0,microsecond=0)
dela_t = y-x

secs = dela_t.seconds+1

t = Timer(secs,run_program)
t.start()



