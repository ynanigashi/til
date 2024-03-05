num_of_inputs = int(input())
inputs = [list(map(int, input().split())) for _ in range(num_of_inputs)]

for input in inputs:
    for i in range(num_of_inputs):
        if input[i] == 1:
            print(i+1, end=' ')
    print()

