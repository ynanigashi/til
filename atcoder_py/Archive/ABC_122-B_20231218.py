import re
input_string = input()
pattern = r'[ACGT]+'
matches = re.findall(pattern, input_string)
print(max([len(match) for match in matches]) if matches else 0)