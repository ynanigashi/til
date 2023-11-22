MAX_AMOUNT = 18000000
MAX_AMOUNT_OF_GROWTH = 12000000
MAX_AMOUNT_OF_TUMI_PER_YEAR = 1200000
MAX_AMOUNT_OF_GROWTH_PER_YEAR = 2400000
# 年数を変更できるようにする
YEARS = 20

def main():
    # 年利も変更できるようにする
    yield_rate = 0.05
    print(f"年利: {yield_rate * 100}%で計算します。")

    while True:
        print("月々の積立投資枠への入金額を入力してください、単位は千円です。")
        print("例/10万円の場合は「100」と入力")
        amount_of_tumi_per_month = int(input(": "))*1000
        if amount_of_tumi_per_month <= MAX_AMOUNT_OF_TUMI_PER_YEAR//12:
            break

        print("月々の積立額は10万円以下にしてください")
    
    while True:
        print("月々の成長投資枠への入金額を入力してください、単位は千円です。")
        amount_of_growth_per_month = int(input(": "))*1000
        if amount_of_growth_per_month <= MAX_AMOUNT_OF_GROWTH_PER_YEAR//12:
            break

        print("月々の積立額は20万円以下にしてください")

    # 変数初期化
    asset_value = 0
    invest_amount = 0
    invest_amount_of_growth = 0
    remain_amount = MAX_AMOUNT
    remain_amount_of_growth = MAX_AMOUNT_OF_GROWTH
    is_invest_end = False
    is_growth_invest_end = False

    # 入力を元に計算し画面に結果を出力する
    for i in range(1, YEARS + 1):
        amount_of_growth_per_year = amount_of_growth_per_month * 12
        # todo:途中から金額を増やすパターンにも対応できるようにする

        if remain_amount_of_growth <= remain_amount:
            # 成長投資枠の制限額を超えたら積立額を0にする
            if invest_amount_of_growth + amount_of_growth_per_year >= MAX_AMOUNT_OF_GROWTH:
                amount_of_growth_per_year = MAX_AMOUNT_OF_GROWTH - invest_amount_of_growth
        else:
            # 投資枠の制限額を超えたら積立額を0にする
            if invest_amount + amount_of_growth_per_year >= MAX_AMOUNT:
                amount_of_growth_per_year = MAX_AMOUNT - invest_amount

        # 年間の投資額を計算
        amount_per_year = amount_of_tumi_per_month * 12 + amount_of_growth_per_year
        
        # MAX_AMOUNTを超えたら積立額を0にする
        if invest_amount + amount_per_year >= MAX_AMOUNT:
            amount_per_year = MAX_AMOUNT - invest_amount
        
        invest_amount_of_growth += amount_of_growth_per_year
        invest_amount += amount_per_year
        asset_value += amount_per_year
        
        # 枠の残り額を計算
        remain_amount = MAX_AMOUNT - invest_amount
        remain_amount_of_growth = MAX_AMOUNT_OF_GROWTH - invest_amount_of_growth

        # 結果を出力
        print(f"{i}年目: {asset_value:,}円")

        # 成長投資枠への入金終了を出力
        if invest_amount_of_growth == MAX_AMOUNT_OF_GROWTH and not is_growth_invest_end:
            print(f"========成長投資枠入金終了==========")
            is_growth_invest_end = True


        # 入金終了を出力
        if invest_amount == MAX_AMOUNT and not is_invest_end:
            print(f"========入金終了==========")
            is_invest_end = True
        
        # 年利を加算する
        asset_value += int(asset_value * yield_rate)

if __name__ == "__main__":
    main()