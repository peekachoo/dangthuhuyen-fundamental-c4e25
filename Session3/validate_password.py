loop = True
while loop:
    mk = input("Enter your password: ")
    loop = False
    if len(mk) < 8:
        loop = True
        print("Password length must be longer than 8. Please enter again.")
    if not mk.isalnum():
        loop = True
        print("Password must not contain special characters. Please enter again.")
    if mk.isdigit():
        loop = True
        print("Password must contain a letter. Please enter again.")
    if mk.isalpha():
        loop = True
        print("Password must contain a digit. Please enter again.")
    print("Please enter again.")

print("Password OK!")