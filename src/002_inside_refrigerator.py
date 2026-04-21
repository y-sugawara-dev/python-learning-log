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

# for i in inside_refrigerator:
#     inside_refrigerator[i] = trim(i)
#     print(inside_refrigerator[1])
