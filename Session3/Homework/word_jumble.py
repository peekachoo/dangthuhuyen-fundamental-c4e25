words = ["daredevil", "spiderman", "jessicajones", "elektra", "ironfist", "lukecage", ]

import random
word = random.choice(words)
jumble = ""
correct_ans = word

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = (word[:position] + word[(position+1):])

print("The jumble is:", jumble)

ans = input("Your answer? ")
while ans != correct_ans:
    print("Wrong answer. Please try again.")
    ans = input()
print("Hooray!")