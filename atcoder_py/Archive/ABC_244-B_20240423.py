_ = input()
commands = input()
directions = ['E', 'S', 'W', 'N']
index = 0
x, y = 0, 0
for c in commands:
    if c == 'R':
        index = (index + 1) % 4
    elif c == 'S':
        direction = directions[index]
        if direction == 'E':
            x += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1
        else:
            y += 1

print(x, y)