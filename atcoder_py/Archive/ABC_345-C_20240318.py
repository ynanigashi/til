from collections import Counter
def count_swaps(s):
    n = len(s)
    return n * (n - 1) // 2

def count_patterns(s):
    total = count_swaps(s)
    for i in range(len(s)):
        ex_char = []
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                total -= 1
                continue
            if s[j] in ex_char:
                total -= 1
            else:
                ex_char.append(s[j])
                
    return total

s = input()
answer = count_patterns(s)
print(max(answer, 1))