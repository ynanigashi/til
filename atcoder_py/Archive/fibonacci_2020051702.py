N = int(input())
fib_list = [0 for _ in range(N)]
fib_list[0] = 0
fib_list[1] = 1
for i in range(len(fib_list[2:])):
    fib_list[i + 2] = fib_list[i + 1] + fib_list[i]
print(fib_list)