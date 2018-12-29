loop_count = 0
while loop_count < 3:
    loop_count += 1
    print("String.")
    print(loop_count)

loop_count = 0
loop = True
while loop:
    loop_count += 1
    print("String.")
    print(loop_count)
    if loop_count >= 3:
        loop = False