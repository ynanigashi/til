words = ('and', 'not', 'that', 'the', 'you')
_ = input()
input_words = list(input().split())
for word in input_words:
    if word in words:
        print('Yes')
        break
else:
    print('No')