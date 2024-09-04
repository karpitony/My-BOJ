import sys
from itertools import product
input = sys.stdin.readline

N = input().strip()
N_set = set(N)

if "0" in N_set:
    N_set.discard("0")

isItSelf = False
for Ns in N_set:
    if int(N) % int(Ns) == 0:
        continue
    else:
        break
else:
    isItSelf = True
    
if isItSelf == True:
    print(N)

else:
    bf_len = 0
    while True:
        for comb in product('0123456789', repeat=bf_len):
            num = int(N + "".join(comb))
            for Ns in N_set:
                if num % int(Ns) == 0:
                    continue
                else:
                    break
            else:
                print(num)
                sys.exit(0)
        bf_len += 1
                