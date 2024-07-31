s = input()
print(s[:s.find('|')]+s[::-1][:s.find('|')][::-1])