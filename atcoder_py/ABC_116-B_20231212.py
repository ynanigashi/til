def transform_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

s = int(input())
# setはハッシュテーブルを使っているため、Listと比べて要素の存在確認が高速
seen_numbers = set()
seen_numbers.add(s)
cnt = 1
while True:
    cnt += 1
    s = transform_num(s)
    if s in seen_numbers:
        print(cnt)
        break
    seen_numbers.add(s)