len_of_sequence = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
set_b = set(b)
same_position = 0
same_number = 0

for i in range(len_of_sequence):
    if a[i] == b[i]:
        same_position += 1
        continue
    if a[i] in set_b:
        same_number += 1

print(same_position)
print(same_number)