len_of_numbers = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = max(a)
min_b = min(b)

print(max(min_b - max_a + 1, 0))