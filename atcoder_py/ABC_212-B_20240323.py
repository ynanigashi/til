pin = list(input())
answer = 'Weak'
if len(set(pin)) != 1:
    for i in range(3):
        if (int(pin[i]) + 1) % 10 != int(pin[i + 1]):
            answer = 'Strong'
            break

print(answer)