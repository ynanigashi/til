num_of_people = int(input())
num_of_days, remain_choco = map(int, input().split())
eten_choco = [1 + (num_of_days-1)//int(input()) for _ in range(num_of_people)]
print(sum(eten_choco) + remain_choco)