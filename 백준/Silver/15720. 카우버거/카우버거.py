import sys
input = sys.stdin.readline

B, C ,D = map(int, input().split())
bugers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

total = sum(bugers) + sum(sides) + sum(drinks)
print(total)

bugers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

min_num = min(B, C, D)
discount = sum(bugers[:min_num] + sides[:min_num] + drinks[:min_num])

etc = total - discount
print(int(discount*0.9) + etc)