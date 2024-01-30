string = input()
len_of_string = len(string)
ans = 'No'
if string == string[::-1]:
    first_half = string[:len_of_string // 2]
    if first_half == first_half[::-1]:
        second_half = string[(len_of_string + 2) // 2:]
        if second_half == second_half[::-1]:
            ans = 'Yes'
print(ans)