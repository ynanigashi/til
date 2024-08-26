left, right = map(int, input().split())
s = input()
print(s[:left-1]+s[left-1:right][::-1]+s[right:])