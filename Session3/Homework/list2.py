sheeps=[5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Ekko and these are my sheep sizes: ")
print(sheeps)
print("")

print("Now my biggest sheep has size", max(sheeps), "let's shear it.")
print("")

m = sheeps.index(max(sheeps)) 
sheeps[m] = 8

print("After shearing, here is my flock: ")
print(sheeps)
print("")


sheeps = [x+50 for x in sheeps]

print("MONTH 1: ")
print("One month has passed, now here is my flock")
print(sheeps)

print("Now my biggest sheep has size", max(sheeps), "let's shear it.")

m = sheeps.index(max(sheeps)) 
sheeps[m] = 8

print("After shearing, here is my flock: ")
print(sheeps)
print("")


sheeps = [x+50 for x in sheeps]

print("MONTH 2: ")
print("One month has passed, now here is my flock")
print(sheeps)

print("Now my biggest sheep has size", max(sheeps), "let's shear it.")

m = sheeps.index(max(sheeps)) 
sheeps[m] = 8

print("After shearing, here is my flock: ")
print(sheeps)
print("")


sheeps = [x+50 for x in sheeps]

print("MONTH 3: ")
print("One month has passed, now here is my flock")
print(sheeps)

print("Now my biggest sheep has size", max(sheeps), "let's shear it.")

m = sheeps.index(max(sheeps)) 
sheeps[m] = 8

print("After shearing, here is my flock: ")
print(sheeps)
print("")


print("My flock has size in total:", sum(sheeps))
print("I would get", sum(sheeps), "* 2$ =", sum(sheeps)*2, "$")

