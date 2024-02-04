s = input()
print(len(s) - s.find('A') - s[::-1].find('Z'))