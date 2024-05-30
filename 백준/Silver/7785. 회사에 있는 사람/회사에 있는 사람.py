n = int(input())
gagle = dict()
name_set = set()

for i in range(n):
    name, status = input().split()
    gagle[name] = status
    name_set.add(name)

name_list = list(name_set)
name_list.sort(reverse=True)

for item in name_list:
    if gagle.get(item) == "enter":
        print(f"{item}")