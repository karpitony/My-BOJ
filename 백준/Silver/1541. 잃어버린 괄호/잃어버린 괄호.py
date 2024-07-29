parse_minus = input().split("-")
for i in range(len(parse_minus)):
    parse_minus[i] = sum(list(map(int, parse_minus[i].split("+"))))
    
result = parse_minus[0]
for i in range(1, len(parse_minus)):
    result -= parse_minus[i]

print(result)