rows = [input() for _ in range(10)]
a, b, c, d = 0, 0, 0, 0
start = False
for i in range(10):
    for j in range(10):
        if rows[i][j] == '#' and start == False:
            a = i
            b = i
            c = j
            d = j
            
            start = True
        elif rows[i][j] == '#' and start == True:
            b = i
            d = j

print(a+1, b+1)
print(c+1, d+1)