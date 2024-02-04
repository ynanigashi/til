num_of_words = int(input())
words = [input() for _ in range(num_of_words)]
for i in range(num_of_words - 1):
    if (words[i][-1] != words[i + 1][0] or 
        words.count(words[i]) > 1 or 
        words.count(words[i + 1]) > 1):
        print('No')
        break
else:
    print('Yes')