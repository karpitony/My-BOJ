num = int(input())

#맵 만들기
game_map=[]
for i in range(1,num+1):
    num_list = list(input().split())
    if '9' in num_list:
        locate_y = i
    game_map.append(num_list)

#아기상어 위치찾기
locate_x = game_map[locate_y].index('9')

bs_locate = [locate_x, locate_y]

print(babyshark_locate)
