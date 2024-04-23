Year = int(input())

if Year % 400 == 0: print(1)
elif Year % 100 == 0: print(0)
elif Year % 4 == 0: print(1)
else: print(0)