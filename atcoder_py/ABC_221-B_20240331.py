string = list(input())
target = list(input())
answer = 'Yes' if string == target else 'No'
for i in range(len(string)-1):
    # swap
    string[i], string[i+1] = string[i+1], string[i]
    if string == target:
        answer = 'Yes'
        break
    # swap back
    string[i], string[i+1] = string[i+1], string[i]

print(answer)