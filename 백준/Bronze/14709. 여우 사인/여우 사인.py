import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    n = map(int, input().split())
    arr.append(n)

fox_count = 0
fox = True
fox_finger_arr=[[1,3],[1,4],[3,4],[3,1],[4,1],[4,3]]
fox_finger = [1,3,4]
non_fox_finger = [2,5]

for a1,a2 in arr:
    if [a1,a2] in fox_finger_arr:
        fox_count += 1
    elif a1 in fox_finger and a2 in non_fox_finger:
        fox = False
        break
    elif a1 in non_fox_finger and a2 in fox_finger:
        fox = False
        break
    
print("Wa-pa-pa-pa-pa-pa-pow!" if fox_count == 3 and fox else "Woof-meow-tweet-squeek")