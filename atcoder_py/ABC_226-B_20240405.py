num_of_inputs = int(input())
sequence = [input() for _ in range(num_of_inputs)]
set_sequence = set(sequence)
print(len(set_sequence))