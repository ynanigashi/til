s = input()
print(s[::-1][:(s[::-1].find('.'))][::-1])