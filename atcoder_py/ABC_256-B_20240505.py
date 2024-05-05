len_of_sequence = int(input())
sequence = list(map(int, input().split()))
position = [0 for _ in range(len_of_sequence)]

for i in range(len_of_sequence):
    num = sequence[i]
    for i in range(0, i+1):
        position[i] += num

print(len([i for i in position if i > 3]))