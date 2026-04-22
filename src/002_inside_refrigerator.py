import csv

# リストを用いたfor文を実際に書いてみる。

# 画面でユーザが冷蔵庫の中の食材を記入し、それをリストで受け取るとする。
# (あまりないと思うが)両端に空白が付いているものの空白を削除してみる。

#画面からうけとったデータを変数にリストで代入
inside_refrigerator = [" 納豆","ヨーグルト　　","鮭の切り身 ","味噌"]

#トリムしてみる。
for index in range(len(inside_refrigerator)):
    inside_refrigerator[index] = inside_refrigerator[index].strip()
    print(inside_refrigerator[index])

# 上のfor文を書く前に下の文を書いた。結果はName Error。
# 「trimという関数は知らない」とのこと。
# なので、AIに助けてもらいつつ、上の文を書いてみたら想定した値を出力することができた。
# また、for文の書き方も併せて修正が必要だった。
# 下の文の場合、iはあくまでもリストから文字列を持ってきていてindexを持ってきているわけではない。
# つまり21行目の[1]でエラーが起こる。
# -----
# for i in inside_refrigerator:
#     inside_refrigerator[i] = trim(i)
#     print(inside_refrigerator[1])
# -----


# 冷蔵庫の中を例として「inside_freezer.csv」というファイルを作成。
# 実際にファイルの中身をリストとして変数に入れ、出力してみる。

# PyQで学習したことを参考に自分で何もみず書いてみたソースが以下
# ---------
# f = open("input/inside_freezer.csv", "r", encoding="utf-8")

# inside_freezer = f.readlines()

# f.close()

# for i in inside_freezer:
#     print("品名：",i[i.0])
# ----------
# 案の定エラー。syntax error。
# 以下を勉強
# ①csvを使うならcsvモジュールを入れることを推奨。
# ②より安全にファイルを管理するならwith open でかくべき

# 以下にAIに教えてもらったことを参考に自分でもう一度書いてみる。

with open("input/inside_freezer.csv", "r",encoding="utf-8") as f:
    inside_freezer = csv.reader(f)
    for row in inside_freezer:
        print("品名：", row[0], "値段", row[1], "賞味期限：", row[2])

# 出力結果は以下のようになり、想定通りに出力することができた。
# -----
# 品名： 食パン 値段 200 賞味期限： 2026/4/29
# 品名： 鶏肉 値段 450 賞味期限： 2026/5/1
# 品名： ねぎ 値段 80 賞味期限： 2026/4/25
# -----