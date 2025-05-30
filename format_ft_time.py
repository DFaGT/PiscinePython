import time
from datetime import datetime

# 現在の秒数（Unixエポックからの経過秒数）を取得
seconds = time.time()

# 通常の浮動小数点数表記と科学的記数法に整形
formatted_seconds = f"{seconds:.4f}"       # 小数点以下4桁まで表示
formatted_scientific = f"{seconds:.2e}"      # 科学的記数法（例: 1.67e+09）

print(f"Seconds since January 1, 1970: {formatted_seconds} or {formatted_scientific} in scientific notation")

# 現在の日付を取得してフォーマット
now = datetime.now()
formatted_date = now.strftime("%b %d %Y")  # 例: Oct 21 2022
print(formatted_date)
