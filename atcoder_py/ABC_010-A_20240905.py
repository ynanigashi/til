trans = {1:0, 2:1, 3:0, 4:1, 5:2, 6:3, 7:0, 8:1, 9:0}
_len_of_input = int(input())
inputs = list(map(int, input().split()))
ans = sum([trans[i] for i in inputs])
print(ans)