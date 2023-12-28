code = input()
code_state = 'Good'
for i in range(len(code)-1):
    if code[i] == code[i+1]:
        code_state = 'Bad'
        break
print(code_state)