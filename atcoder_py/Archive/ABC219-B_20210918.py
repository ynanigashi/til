def transform(x, p):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    str = ""
    for c in p:
        str += abc[x.find(c)]
    return str

x = input()
n = int(input())
people = [input() for _ in range(n)]
people.sort(key=lambda p: transform(x, p))

for p in people:
    print(p)