list= [1, 2, 4, 8, 16, 32, 64]
n = int(input())

for i in list[::-1]:
    if n >= i:
        print(i)
        break