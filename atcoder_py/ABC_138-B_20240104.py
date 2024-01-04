len_of_numbers = int(input())
inverse_numbers = list(map(lambda n: 1/int(n), input().split()))
print(1/sum(inverse_numbers))