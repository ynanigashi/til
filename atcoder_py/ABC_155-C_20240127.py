num_of_words = int(input())
words ={}
for i in range(num_of_words):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1],x[0]))
max_num = sorted_words[0][1]
for word, num in sorted_words:
    if num == max_num:
        print(word)
    else:
        break