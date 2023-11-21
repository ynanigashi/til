MAX_AMOUNT = 20000000
# GROWTH枠を利用した場合も計算出来るようにする
MAX_AMOUNT_PER_YEAE = 1200000
# 年数を変更できるようにする
YEARS = 20

def main():
    # 年利も変更できるようにする
    yield_rate = 0.05
    print(f"年利: {yield_rate * 100}%で計算します。")

    while True:
        # 千円単位で入力を受け付けた方がいいかも
        amount_per_month = int(input("月々の積立額を入力してください: "))
        if amount_per_month <= MAX_AMOUNT_PER_YEAE//12:
            break

        print("月々の積立額は10万円以下にしてください")

    # 入力を元に計算し画面に結果を出力する
    asset_value = 0
    invest_amount = 0
    is_invest_end = False
    for i in range(1, YEARS + 1):
        amount_per_year = amount_per_month * 12
        
        # 2000万円までは一年間の積立額を加算する
        if invest_amount + amount_per_year >= MAX_AMOUNT:
            amount_per_year = MAX_AMOUNT - invest_amount
        
        # 2000万円を超えたら積立額を0にする
        invest_amount += amount_per_year
        asset_value += amount_per_year

        # 結果を出力
        print(f"{i}年目: {asset_value:,}円")

        # 入金終了を出力
        if amount_per_year != amount_per_month*12 and is_invest_end == False:
            print(f"========入金終了==========")
            is_invest_end = True
        
        # 年利を加算する
        asset_value += int(asset_value * yield_rate)

if __name__ == "__main__":
    main()
