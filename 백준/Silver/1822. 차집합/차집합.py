nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(set(A) - set(B))
lenList = len(result)

if lenList == 0:
    print(0)
else:
    result.sort()
    print(lenList)
    for i in result:
        print(i, end = " ")