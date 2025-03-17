import sys

input = sys.stdin.readline

N = int(input())

year = 2024
month = 8

for i in range(N-1):
    month += 7
    if month > 12:
        year += 1
        month -= 12

print(year, month)