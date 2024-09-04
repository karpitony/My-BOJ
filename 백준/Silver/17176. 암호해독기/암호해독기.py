import sys
input = sys.stdin.readline

N = int(input())
encrypt = list(map(int, input().split()))
decrypt = input().strip()

check = []
for de in decrypt:  
    if de == ' ':
        check.append(0)
        continue

    ascii_de = ord(de)
    if ascii_de >= 97 and ascii_de <= 122:
        # a ~ z 소문자
        check.append(ascii_de-70)
    elif ascii_de >= 65 and ascii_de <= 90:
        # A ~ Z 대문자
        check.append(ascii_de-64)


encrypt.sort(); check.sort()
result = "y" if encrypt == check else "n"
print(result)