n = int(input("Enter n = "))

if n > 13:
    print (n, "> 13")
else:
    print (n, "< 13")

from random import randint
print(randint(1, 100))

weather = randint(1,100)

if weather <= 30:
    print("Rainy")
elif weather <= 60:
    print("Cloudy")
else:
    print("Sunny")