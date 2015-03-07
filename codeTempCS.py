#this is my first attempt at developing a python program of any kind
#it runs but I'd like to put date before time
#and time on a separate line below date

import datetime

currentDate = datetime.datetime.today()
print(currentDate)
print(currentDate.strftime('%d %b %y'))

inp = input('Enter Fahrenheit Temperature:')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print (cel)

inp = input('Enter Celsius Temperature:')
cel = float(inp)
fahr = ( cel * 9.0 ) / 5.0 + 32.0
print (fahr)
