# 你有一份学生数据，需要处理并保存结果。
import pandas as pd
import json

students = [
    {"name": "Alice", "score": 82, "comment": "doing well"},
    {"name": "Bob", "score": 45, "comment": None},
    {"name": "Charlie", "score": 91, "comment": "excellent"},
    {"name": "Di", "score": 58, "comment": "[deleted]"},
    {"name": "Eve", "score": 73, "comment": "needs improvement"},
]

# 任务：
# 把 students 转成 DataFrame
# 加一列 name_len，存每个名字的字符数
# 加一列 comment_valid，comment 不是 None 也不是 "[deleted]" 的为 True，否则为 False
# 筛出 score 大于 60、且 comment_valid 为 True 的行，存进 df_filtered，记得加 .copy()
# 检查 df_filtered 是否为空，如果空就打印 "没有符合条件的学生" 然后结束
# 不为空的话，用 f-string 打印："符合条件的学生共 X 名"（X是实际数量）
# 把 df_filtered 存成 result.csv
# 把一个字典 {"total": X, "names": [...]} 写进 result.json，X 是人数，names 是符合条件的名字列表

