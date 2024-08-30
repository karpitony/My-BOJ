N = input()
arr = [n for n in N]
arr.sort(reverse=True)
for _ in arr:
    print(_,end='')
