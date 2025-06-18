import sys
input = sys.stdin.readline


def str_to_min(timeString: str) -> int:
    hour, min = map(str, timeString.split(":"))
    return hour * 60 + min

S, E, Q = map(str, input().split())

S = str_to_min(S)
E = str_to_min(E)
Q = str_to_min(Q)

start_attendance = set()
end_attendance = set()
result = set()

while True:
    try:
        t, name = map(str, input().split())
        t = str_to_min(t)
        if t <= S:
            start_attendance.add(name)
        elif t >= E and t <= Q:
            end_attendance.add(name)
        else:
            continue
    except:
        break
    
result = start_attendance.intersection(end_attendance)
print(len(result))