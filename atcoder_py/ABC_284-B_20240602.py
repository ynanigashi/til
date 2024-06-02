num_of_tests = int(input())
for _ in range(num_of_tests):
    _ = input()
    seqs = list(map(int, input().split()))
    cnt = 0
    for i in seqs:
        if i % 2 == 1:
            cnt += 1
    
    print(cnt)

