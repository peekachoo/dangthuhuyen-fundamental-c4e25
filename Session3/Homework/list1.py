items = ["T-Shirt", "Sweater"]
print("Welcome to our shop, what do you want?")
print("Our items: ", end="")
print(*items, sep=", ")

print("Welcome to our shop, what do you want?")
items.append(input("Enter new item: "))
print("Our items: ", end="")
print(*items, sep=", ")

print("Welcome to our shop, what do you want?")
n = int(input("Update position? "))
items[n-1] = input("New item? ")
print("Our items: ", end="")
print(*items, sep=", ")

print("Welcome to our shop, what do you want?")
i = int(input("Delete position? "))
items.pop(i-1)
print("Our items: ", end="")
print(*items, sep=", ")