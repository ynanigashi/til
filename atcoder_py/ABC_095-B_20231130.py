num_of_dounut_types, gram_of_flour = map(int, input().split())
dounut_types = [int(input()) for _ in range(num_of_dounut_types)]
dounut_types.sort()
num_of_dounuts = len(dounut_types)
gram_of_flour -= sum(dounut_types)
num_of_dounuts += gram_of_flour // dounut_types[0]
print(num_of_dounuts)