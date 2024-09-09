import sys
input = sys.stdin.readline

word = input().strip()
line1 = ""; line2 = ""; line3 = "";

def arr_append(diaOrStar:str, alphabet:str):
    global line1, line2, line3
    if line3 == "":
        line1 += f"..{diaOrStar}.."
        line2 += f".{diaOrStar}.{diaOrStar}."
        line3 += f"{diaOrStar}.{alphabet}.{diaOrStar}"

    elif line3[-1] == "#" and diaOrStar == "*":
        line1 += f".{diaOrStar}.."
        line2 += f"{diaOrStar}.{diaOrStar}."
        line3 = line3.rstrip("#")
        line3 += f"{diaOrStar}.{alphabet}.{diaOrStar}"
        
    else:
        line1 += f".{diaOrStar}.."
        line2 += f"{diaOrStar}.{diaOrStar}."
        line3 += f".{alphabet}.{diaOrStar}"

for i in range(len(word)):
    if (i + 1) % 3 == 0:
        arr_append("*", word[i])
    else:
        arr_append("#", word[i]) 
        
print(line1)
print(line2)
print(line3)
print(line2)
print(line1)