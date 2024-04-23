N = int(input())

if N == 1:  # 1 거르기
    None

else:
    for i in range(2, N+1):
        while True:
            if N % i == 0:
                print(i)
                N /= i
            else:
                break