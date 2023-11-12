height, width = map(int, input().split())
lines = [input() for _ in range(height)]

print('#' * (width + 2))
for line in lines:
    print('#' + line + '#')
print('#' * (width + 2))