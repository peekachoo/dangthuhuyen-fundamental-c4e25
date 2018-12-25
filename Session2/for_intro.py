n = int(input("Enter n = "))
for i in range(1, n+1):
    print(i)

m = int(input("Enter m = "))
for i in range(0, m+1, 2):
    print(i)

from turtle import *

for i in range(20):
    forward(i * 10)
    left(90)

mainloop()
