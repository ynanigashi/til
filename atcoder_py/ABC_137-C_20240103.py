#TLEです！
def is_anagram(str1, str2):
    for c in set(str1):
        if str1.count(c) != str2.count(c):
            break
    else:
        return True
    
    return False

num_of_strings = int(input())
strings = [input() for _ in range(num_of_strings)]
ans = 0
for i in range(num_of_strings-1):
    for j in range(i + 1, num_of_strings):
        if is_anagram(strings[i], strings[j]):
            ans += 1

print(ans)
        