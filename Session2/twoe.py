
from turtle import *

l = int(input("Enter l = "))
j = 0
for i in range(l+1):
    for i in range(2):
        forward(10+j)
        left(90)
    forward(10+j)
    j = j + 10
    forward(10)
    left(90)

mainloop()