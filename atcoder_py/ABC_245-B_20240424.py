len_of_sequence = int(input())
sequence = set(list(map(int, input().split())))
for i in range(2002):
    if i not in sequence:
        print(i)
        break
