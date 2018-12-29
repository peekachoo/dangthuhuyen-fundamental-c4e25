from turtle import *

speed(0)

pencolor('blue')
for i in range(4):
   left(90)
   forward(100)

pencolor('yellow')
for i in range(5):
   left(60)
   forward(100)

pencolor('red')
left(120)
forward(100)
right(120)
forward(100)

left(132)

pencolor('brown')
for i in range(4):
   forward(100)
   left(72)

pencolor('grey')
for i in range(7):
    forward(100)
    left(180 - 128.57)

mainloop()