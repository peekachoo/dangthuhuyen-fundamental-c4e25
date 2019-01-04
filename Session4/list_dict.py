p1 = {
    "nickname": "L",
    "yob": 1991
}

p2 = {
    "nickname": "N",
    "yob": 1999
}

p3 = {
    "nickname": "M",
    "yob": 1995
}

p_list = [] # p_list = [p1, p2, p3]

# p_list = [
#     {
#         "nickname": "L",
#         "yob": 1991
#     }
#     {
#         "nickname": "N",
#         "yob": 1999
#     }
#     {
#         "nickname": "M",
#         "yob": 1995
#     }
# ]

print(p_list)

p_list.append(p1)
print(p_list)

p_list.append(p2)
p_list.append(p3)
print(p_list)

# p_first = p_list[0]
# print(p_first)
# print(p_first["nickname"])

for p in p_list:
    print(p["nickname"], p["yob"])