len_of_numbers = int(input())
numbers = [int(input()) for _ in range(len_of_numbers)]
max_num = max(numbers)
max_num_index = numbers.index(max_num)
second_num = max(numbers[:max_num_index] + numbers[max_num_index+1:])

for i in range(len_of_numbers):
    print(second_num if i == max_num_index else max_num)
