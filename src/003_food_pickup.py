# 実際にファイルの中身から色々な条件でピックアップして表示してみる。
# 002のファイルと似たようなことを実施するが使用するテストデータは増やしてある。
# 今回使用するテストデータはAIに作成してもらった。賞味期限が自分で作った時は
# yyyy/mm/ddの型だったが、AIはyyyy-mm-ddだった。
# 文字列比較の際にバグに繋がる危険性があるとのことで、基本的にはyyyy-mm-ddの型でいいと学習。

# 使用するライブラリをインポート
import csv
from datetime import date

# ファイル作成時にファイル名に今日の日付を入れたい。なのであらかじめ変数で持っておく。
today_str = date.today().strftime("%Y%m%d")

# ①賞味期限が切れている商品をピックアップしてみる。
# PyQではwithopenは2026/5/13時点で学習していないが、こちらの方が実務的なためこちらを使用する。
# -----プログラムはここから-----
# with openでファイルを開く。
with open("input/foods.csv", "r", encoding="utf-8") as f:
    # 変数初期化
    foods_list = csv.reader(f)
    expired_list = []
    count = 0
    # for文で繰り返す際に賞味期限リストを作成
    for row in foods_list:
        name = row[0]
        price = row[1]
        expiry = row[2]
        if date.fromisoformat(expiry) <= date.today():
            expired_list.append([name, price, expiry])
            count += 1
    # 1件でも賞味期限切れの品名があった場合、コンソールに出力かつCSVファイルをプログラム実行日付を付け加えて作成
    if count >= 1:
        print("賞味期限切れの品があります！")
        for item in expired_list:
            print(",".join(item))
        with open(f"output/expired_list_{today_str}.csv", "w", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(["品名","値段","賞味期限"])
            writer.writerows(expired_list)
# -----プログラムはここまで-----
# AIに教えてもらいつつ想定通りの結果を出すことができた。
