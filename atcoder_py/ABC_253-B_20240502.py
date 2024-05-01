height, width = map(int, input().split())
rows = [input() for _ in range(height)]
maru_1 = [0, 0]
maru_2 = [0, 0]
maru_1_flag = True
for i in range(height):
    for j in range(width):
        if rows[i][j] == '-':
            continue
        if maru_1_flag == True:
            maru_1[0] = i
            maru_1[1] = j
            maru_1_flag = False
        else:
            maru_2[0] = i
            maru_2[1] = j
        
print(abs(maru_1[0] - maru_2[0]) + abs(maru_1[1] - maru_2[1]))