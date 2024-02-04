_ = input()
command = input()
x, max_x = 0, 0
for c in command:
    if c == 'I':
        x += 1
    else:
        x -= 1
    
    max_x = x if max_x < x else max_x

print(max_x)