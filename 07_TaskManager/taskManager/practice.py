lists = {
    "a" : [],
    "b" : [],
}

for i in range(1,10):
    if i%2==0:
        lists["a"].append(i)
    else:
        lists["b"].append(i)

print(lists)