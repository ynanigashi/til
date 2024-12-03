num_of_inputs = int(input())
sequence = list(map(int, input().split()))
print(max(sequence) - min(sequence))