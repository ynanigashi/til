def count_digits(n):
    """
    整数 n の桁数をカウントする関数
    """
    # 整数を絶対値に変換（負の数の場合を考慮）
    n = abs(n)

    # カウントアップするための変数
    count = 0

    # 整数が0になるまで10で割り続ける
    while n > 0:
        n //= 10  # 整数を10で割り、結果を整数にする
        count += 1  # カウンターを増やす

    # 整数が1桁の場合、ループは実行されないため、カウントを1に設定
    if count == 0:
        count = 1

    return count

n = int(input())
ans = 0
len_of_digits = count_digits(n)

if len_of_digits == 6:
    ans = 90909
elif len_of_digits == 5:
    ans = 909
    ans += n - 9999
elif len_of_digits == 4:
    ans = 909
elif len_of_digits == 3:
    ans = 9
    ans += n - 99
elif len_of_digits ==2:
    ans = 9
elif len_of_digits ==1:
    ans = n

print(ans)