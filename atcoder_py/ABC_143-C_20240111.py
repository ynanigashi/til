num_of_slimes = int(input())
slime_colors = input()
slime_color = ''
ans = 0
for c in slime_colors:
    if c != slime_color:
        ans += 1
        slime_color = c

print(ans)