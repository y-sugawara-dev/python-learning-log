# 勤務表を加工して、別ファイルとして出力してみる。
# 誤差が最小限になるように、Decimalで計算してみる。

# 必要なモジュールをインポート
import csv
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# 変数初期化
hourly_wage = Decimal("1150")
total_time = Decimal("0")
details = []

# ファイルを開く
with open("input/timecard.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f) 
    next(reader) #ヘッダーをスキップ
    
    for row in reader:
        date = row[0]
        start_time = row[1]
        end_time = row[2]

        # 開始時間を変数にdatetime型で代入
        start = datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
        # 終了時間を変数にdatetime型で代入
        end = datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")

        # 勤務時間を計算し、変数に代入。勤務時間合計及び給与計算で使用できるよう秒で保持。
        work_seconds = Decimal(str((end - start).total_seconds()))

        # 総勤務時間
        total_time += work_seconds

        # hh:mmに整形
        hours = int(work_seconds // 3600)
        minutes = int((work_seconds % 3600) // 60)
        work_hm = f"{hours:02d}:{minutes:02d}"
        # 明細をリストで保持。
        details.append(f"{date}, {start_time}, {end_time}, {work_hm}")

# 総勤務時間をhh:mmに整形
total_hours = int(total_time // 3600)
total_minutes = int((total_time % 3600) // 60)
total_hm = f"{total_hours:02d}:{total_minutes:02d}"

# 給料計算
total_hours_decimal = (total_time / Decimal("3600")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
saraly =(hourly_wage * total_hours_decimal).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        
# ファイルに書き込んで保存
with open("output/timecard.txt", "w", encoding="utf-8") as f:
    f.write("勤務表\n")
    f.write(f"勤務時間合計：{total_hm}時間\n")
    f.write(f"支給金額：{saraly:,}円\n")
    f.write("--詳細--\n")
    f.write("日付, 開始時刻, 終了時刻, 勤務時間\n")
    for detail in details:
        f.write(f"{detail}\n")