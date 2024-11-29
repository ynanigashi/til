heigt, width = map(int, input().split())
top_bottom = '#' * (width + 2)
print(top_bottom)
for _ in range(heigt):
    print('#' + input() + '#')
print(top_bottom)