num_of_candy_bags = list(map(int, input().split()))
is_fair = max(num_of_candy_bags)*2 == sum(num_of_candy_bags)
answer = 'Yes' if is_fair else 'No'
print(answer)
