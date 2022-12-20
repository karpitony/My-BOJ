'''
f를 받아서 배열에서 f개많큼 뽑고 그중 가장 작은 값xf 한게 넓이
가장 큰 넓이를 저장해서 비교하면서 바꿈

지금은 대충 해놔서 h값에 가장 작은 값 넣는거부터 하면 됨
'''
N= int(input())
height=[]
for i in range(0,N):
    T=int(input)
    heigth.append(T)

area=0
for f in range(1,N+1):
    for g in range(1,N+1):
        h=

        temp=f*h
        
        if temp>area:
            area=temp
