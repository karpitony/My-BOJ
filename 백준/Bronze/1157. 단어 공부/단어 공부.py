word = input().upper()
word_dict = {}

for char in word:
    word_dict[char] = word_dict.get(char, 0) + 1
    
max_value = max(word_dict.values())
max_key = []
for k, v in word_dict.items():
    if v == max_value:
        max_key.append(k)
        
if len(max_key) > 1:
    print("?")
else:
    print(max_key[0])
