max_len = int(input())
s = input()
print(s if len(s) <= max_len else s[:max_len] + '...')