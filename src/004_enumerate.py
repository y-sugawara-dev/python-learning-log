# enumerate()を使用してリストに行番号を先頭につけて出力してみる。

# 使用するライブラリをインポート
import csv

with open("python-learning-log/input/foods.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for n, line in enumerate(lines):
        print(f"{n}:{line.rstrip()}")
        
    