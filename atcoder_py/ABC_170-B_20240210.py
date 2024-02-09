num_of_animals, num_of_legs = map(int, input().split())
ans = 'No'
for i in range(num_of_animals+1):
    if (num_of_animals-i)*4+i*2 == num_of_legs:
        ans = 'Yes'
        break
print(ans)