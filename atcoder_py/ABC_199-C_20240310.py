def swap(s, a, b):
    s[a], s[b] = s[b], s[a]
    return s

def swap_half(s, half_len_of_str):
    s[:half_len_of_str], s[half_len_of_str:] = s[half_len_of_str:], s[:half_len_of_str]
    return s

half_len_of_str = int(input())
s = list(input())
num_of_query = int(input())
is_swapped = False
for _ in range(num_of_query):
    t, a, b = map(int, input().split())
    if t == 1:
        if is_swapped:
            a = a + half_len_of_str if a <= half_len_of_str else a - half_len_of_str
            b = b + half_len_of_str if b <= half_len_of_str else b - half_len_of_str
        s = swap(s, a-1, b-1)
    else:
        is_swapped = not is_swapped


if is_swapped:
    s = swap_half(s, half_len_of_str)

print(''.join(s))