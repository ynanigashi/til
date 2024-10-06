s = input()
k = int(input())
s_len = len(s)
s_set = set()
for i in range(s_len - k + 1):
    s_set.add(s[i:i+k])
print(len(s_set))