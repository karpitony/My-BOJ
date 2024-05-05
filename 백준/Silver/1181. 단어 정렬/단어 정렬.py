N = int(input())
word = list()
for i in range(N):
    word.insert(i, input())

temp = set(word)    # 중복 제거
word = list(temp)

word_dict = {}
for w in word:
    length = len(w)
    if length not in word_dict:
        word_dict[length] = []
    word_dict[length].append(w)


for key in sorted(word_dict.keys()):  
    word_list = sorted(word_dict[key])  
    for word in word_list:
        print(word)