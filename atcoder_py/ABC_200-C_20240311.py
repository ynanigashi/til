len_of_numbers = int(input())
numbers = list(map(int, input().split()))
mod_numbers = [i % 200 for i in numbers]
set_mod_numbers = set(mod_numbers)
mod_numbers_count = [mod_numbers.count(i) for i in set_mod_numbers]
count = 0
for i in mod_numbers_count:
    count += i * (i - 1) / 2
print(int(count))