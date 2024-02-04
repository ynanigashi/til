import re
a, b = map(int, input().split())
input_str = input()
# escape curly braces curly braces
regex_pattern = fr"^\d{{{a}}}-\d{{{b}}}$"
print("Yes" if re.match(regex_pattern, input_str) else "No")