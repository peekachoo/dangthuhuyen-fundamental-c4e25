# # R
death_note = {
    "rule1": "If someone's name is written in the note, they'll be dead in 40 seconds.",
    "rule2": "The writer have to know the face of the people they write.",
    "rule3": "The writer can decide the reason of the death by writing it in the note in the next 40 seconds.",
}
# for i in death_note:
#     print(i, end="      ")

# print()
# n = input("Code? ").lower()
# print(death_note[n])


# # U 
# ans = input("Do you want to update? Y/N ").upper()
# if ans == "Y":
#     upd = input("Update rule? ").lower()
#     death_note[upd] = input("Enter new rule: ")
# print(death_note)


# # C - giong Update(neu key ton tai: update, neu key k ton tai: create)
# death_note["rule4"] = "Bla bla bla bla"


# kiem tra xem key co ton tai hay khong
rule = input("Enter rule: ").lower()
if rule in death_note:
    print("Rule exists.")
else:
    ans = input("Not exists. Contribute? Y/N ").upper()
    if ans == "Y":
        death_note[rule] = input("Enter new rule: ")
print(death_note)
# muon lap lai -> while True:

# D
del death_note["rule3"]
