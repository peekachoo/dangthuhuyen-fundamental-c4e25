from random import randint
n = randint(1, 100)

lan = 0
x = int(input("Enter x from 1 to 100 (you have 3 guesses): "))

while x != n and lan < 2:
    lan += 1
    if x < n:
        print("Wrong number. Try again.")
    else:
        print("Wrong number. Try again.")
    x = int(input("Enter x from 1 to 100: "))

if lan < 2:
    print("Bingo!")
else:
    print("You lose.")