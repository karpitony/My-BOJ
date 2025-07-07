import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums_order = list(set(nums))
nums_order.sort()
zip_nums = { nums_order[i]:i for i in range(len(nums_order))}
for n in nums:
    print(zip_nums[n], end=" ")