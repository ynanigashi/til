_ = input()
nums = list(map(int, input().split()))
cnt = 0
while True:
    for i in range(len(nums)):
        if nums[i] % 2 == 1: break
        # /= だとfloatになるため
        nums[i] //= 2
    else:
        cnt += 1
        continue
    break

print(cnt)