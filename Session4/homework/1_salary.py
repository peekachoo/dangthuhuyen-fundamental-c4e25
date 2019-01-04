dic = {
    "name": ["Huy", "Quan", "Duc",],
    "salary": [25, 25, 30],
    "hours": [30, 20, 40],
}

s = 0
total = 0

for k in dic["salary"]:
    salperhour = k * dic["hours"][s]
    print("Luong hang tuan cua", dic["name"][s], "la:", salperhour)
    s += 1
    total += salperhour

print("Tong luong:", total)