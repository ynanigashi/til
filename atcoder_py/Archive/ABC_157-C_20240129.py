num_of_digits, num_of_inputs = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(num_of_inputs)]
ans = -1
# 対象の桁数の最小値を求める (1桁の場合は0を含む)
range_min = 10 ** (num_of_digits -1) if num_of_digits > 1 else 0
# 対象の桁数の数字を下から順に見ていき、条件を満たすものがあればそれを答えとする
for i in range(range_min, 10 ** num_of_digits):
    i = str(i)
    for input in inputs:
        if i[input[0] - 1] != str(input[1]):
            break
    else:
        ans = i
        break

print(ans)