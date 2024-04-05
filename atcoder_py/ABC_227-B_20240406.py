num_of_answers=int(input())
answers=list(map(int,input().split()))

count = 0
for answer in answers:
  flag=False
  for a in range(1,1001):
    for b in range(1,1001):
      if 4*a*b+3*a+3*b==answer:
        flag=True
  if not flag:
    count += 1

print(count)