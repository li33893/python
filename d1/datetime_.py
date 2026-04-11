"""

    datetime


"""

from datetime import datetime

# datetime → 时间戳
dt = datetime(2023, 1, 1)
timestamp = int(dt.timestamp())
print(f"datetime转时间戳：{timestamp}")

# 时间戳 → datetime
dt2 = datetime.fromtimestamp(timestamp)
print(f"时间戳转datetime：{dt2}")