_, num_of_sticks_to_use = map(int, input().split())
length_of_sticks = list(map(int, input().split()))
length_of_sticks.sort(reverse=True)
print(sum(length_of_sticks[:num_of_sticks_to_use]))