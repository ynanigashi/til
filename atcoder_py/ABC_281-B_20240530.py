import re
s = input()
print('Yes' if re.match(r'^[A-Z][1-9][0-9]{5}[A-Z]$', s) else 'No')
