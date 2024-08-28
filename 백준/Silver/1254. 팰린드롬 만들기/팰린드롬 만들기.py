word = input()
if word[::-1] == word:
    print(len(word))
else:  
    for i in range(1, len(word)+1):
        word2 = word + word[:i][::-1]
        if word2 == word2[::-1]:
            print(len(word2))
            break