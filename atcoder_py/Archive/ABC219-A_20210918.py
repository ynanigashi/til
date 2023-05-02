x = int(input())
ans = 'expert'
if x >= 90:
  pass
elif x >= 70:
    ans = 90 - x
elif x >= 40:
    ans = 70 - x
else:
    ans = 40 - x
print(ans)