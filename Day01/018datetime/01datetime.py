# Python Datetime

import datetime

x = datetime.datetime.now()
print(x)  #2023-02-09 18:51:36.822133
print(x.year) # will return year
print(x.strftime("%A")) # will return name of the weekday

print('----------------strftime method----------------------------')
print(x.strftime(''))
# Creating Date object
x = datetime.datetime(2023, 2, 9)  #Thursday Feb 9, 2023
print("Todays date: Thursday Feb 9, 2023")
print("x =>", x)   # 2023-02-09 00:00:00
print("x.strftime('%a') => ", x.strftime('%a')) #Thu
print("x.strftime('%A' => ", x.strftime('%A')) #Thursday
print("x.strftime('%w') => ", x.strftime('%w')) # 4
print("x.strftime('%b') => ", x.strftime('%b')) #Feb
print("x.strftime('%B') => ",x.strftime('%B')) #Febuarary
print("x.strftime('%m') => ", x.strftime('%m')) # 02
print("x.year => ", x.year) # 2023
print("x.strftime('%Y') => ", x.strftime('%Y')) # 2023
print("x.strftime('%y') => ", x.strftime('%y')) # 23


