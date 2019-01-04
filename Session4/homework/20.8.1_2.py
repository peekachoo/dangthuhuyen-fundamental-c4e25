# Dung ham
import collections

x = input("Enter a string: ").lower()
c = collections.Counter(x)
del c[" "]

for letter, count in sorted(c.items()):
    print(letter, count, sep="  ")