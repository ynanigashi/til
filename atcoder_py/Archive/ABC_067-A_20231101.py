a, b = map(int, input().split())
is_possible = a%3==0 or b%3==0 or (a+b)%3==0
print('Possible' if is_possible else 'Impossible')