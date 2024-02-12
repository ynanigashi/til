import itertools
height, width, num_of_black = map(int, input().split())
cells = [list(input()) for _ in range(height)]
# print(cells)

# 組み合わせを作成
combinations = []
# rowからの選択パターン
for r in range(height + 1):
    for subset1 in itertools.combinations(range(height), r):
        # columnからの選択パターン
        for s in range(width + 1):
            for subset2 in itertools.combinations(range(width), s):
                combinations.append((subset1, subset2))


# print(combinations)

# 組み合わせを使って黒マスを数える
count = 0
for combination in combinations:
    temp_num_of_black = 0
    for i in range(height):
        for j in range(width):
            # 組み合わせに含まれる場合はスキップ
            if i in combination[0] or j in combination[1]:
                continue
            if cells[i][j] == '#':
                temp_num_of_black += 1
    if temp_num_of_black == num_of_black:
        count += 1

print(count)