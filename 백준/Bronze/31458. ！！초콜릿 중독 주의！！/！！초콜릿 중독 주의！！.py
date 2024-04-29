T = int(input())

def slice_strL(str, loc):
    if loc != 0:
        strL = str[:loc]
        return strL
    else:
        return ''


for i in range(T):
    
    str = input()
    find0 = str.find('0')
    find1 = str.find('1')
    
    if find1 == -1:     # 1이 없다 = n이 0이다.
        n = 0
        strL = slice_strL(str, find0)
        strR = str[find0+1:]
    else:               # n이 1이다.
        n = 1
        strL = slice_strL(str, find1)
        strR = str[find1+1:]
    
    # n이 팩토리얼 거쳐서 0되는지, 1되는지
    if n == 0 and len(strR) > 0:
        n = 1

    if n == 0:
        if len(strL) == 0:
            n = 0
        elif len(strL) % 2 == 0:
            n = 0
        else:
            n = 1
    else:
        if len(strL) == 0:
            n = 1
        elif len(strL) % 2 == 0:
            n = 1
        else:
            n = 0
            
    print(n)