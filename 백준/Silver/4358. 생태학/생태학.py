import sys
input = sys.stdin.readline

d1 = dict()
sum = 0
while True:
    tree = input().split('\n')
    if not tree[0]:
        break;
    sum += 1
    d1[tree[0]] = d1.setdefault(tree[0], 0) + 1

d2 = sorted(d1.items(), key=lambda x:x[0])
d2 = dict(d2)
for k, v in d2.items():
    percent = round((v / sum) * 100, 4)
    print(k + " {:.4f}".format(percent))