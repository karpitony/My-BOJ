import math
print('\n'.join(str(math.lcm(*map(int, input().split()))) for _ in range(int(input()))))