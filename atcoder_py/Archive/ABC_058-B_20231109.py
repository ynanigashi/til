odd_str = input()
even_str = input()
password = ''
for i in range(len(even_str)):
    password += odd_str[i] + even_str[i]

if len(odd_str) > len(even_str):
    password += odd_str[-1]

print(password)