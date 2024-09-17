num_of_towns = int(input())
a, b = map(int, input().split())
num_of_inputs = int(input())
inputs = list(map(int, input().split()))
inputs.insert(0, a)
inputs.append(b)
if len(set(inputs)) == len(inputs):
    print('YES')
else:
    print('NO')