S = int(input())
T=0
result=0
for i in range(1,S+1):
    result+=i
    T+=1
    if(result > S):
        T -= 1
        break
print(T)