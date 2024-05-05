N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))

    # 박스 수와 현재 무게 초기화
    box = 1
    weight = 0

    for book in books:
        if weight + book > M:
            box += 1
            weight = book
        else:
            weight += book

    print(box)