num_of_names, max_num = map(int, input().split())
names = [input() for _ in range(num_of_names)]
limited_names = sorted(names[:max_num])
for name in limited_names:
    print(name)
