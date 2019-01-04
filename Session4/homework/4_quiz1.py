ques = {
    "Answer the following algebra question: \nIf x = 8, then what is the value of 4(x + 3) ? \n1. 35 \n2. 36 \n3. 40 \n4. 44": 4,
}

for k in ques.keys():
    print(k)
    x = int(input("Your choice: "))
    while x != ques[k]:
        print(":( \n")
        print(k)
        x = int(input("Your choice: "))
    else:
        print("Bingo!")