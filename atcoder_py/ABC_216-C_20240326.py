n = int(input())
answer = ''
while n > 0:
    if n % 2 == 1:
        answer += 'A'
        n -= 1
    else:
        answer += 'B'
        n //= 2

print(answer[::-1])