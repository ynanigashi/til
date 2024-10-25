num_of_inputs, length = map(int, input().split())
inputs = [input() for _ in range(num_of_inputs)]
inputs.sort()
print("".join(inputs))