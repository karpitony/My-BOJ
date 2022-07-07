case = int(input())
for a in range(case):
    num = list(map(str,input().split()))
    answer=0
    for i in range(0,len(num)):
        if i==0:
            answer=float(num[i])
        else:
            if num[i]=="@":
                answer=answer*3
            elif num[i]=="%":
                answer=answer+5
            elif num[i]=="#":
                answer=answer-7
    print(format(answer, '.2f'))
