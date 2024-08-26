num_of_input = int(input())
sweet = 0
for _ in range(num_of_input):
    taste = input()
    if taste == 'sweet':
        sweet += 1
    else:
        sweet = 0
    
    if sweet >= 2:
        break
else:
    print('Yes')
    exit()

print('No')