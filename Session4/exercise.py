number = [34, 90, 76, 3, 1, 9, 13, 21, 26, 33, 49, 80]
# print(number.index(min(number)), min(number), sep=". ")

minn = 34

for i in range(len(number)):
    if minn > number[i]:
        minn = number[i]
        min_index = i

print(min_index, minn, sep=". ")