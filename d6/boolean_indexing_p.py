#  1. 理解题： 下面的代码会保留哪几行？
# data = {"name": ["Alice", "Bob", "Charlie", "Diana"],
#         "score": [90, 45, 70, 55]}
# df = pd.DataFrame(data)

# result = df[(df["score"] >= 60) & (df["score"] <= 80)]




#  2. 操作题： 从下面的 df 里筛出名字长度大于3、且 age 大于等于18的行，打印结果：
# import pandas as pd

# data = {"name": ["Alice", "Bob", "Charlie", "Di"],
#         "age": [25, 17, 30, 20]}
# df = pd.DataFrame(data)



#  3. 加强题：
import pandas as pd

data = {
    "product": ["apple", "banana", "kiwi", "strawberry", "fig"],
    "price": [1.5, 0.8, 3.2, 2.1, 4.0],
    "in_stock": [True, False, True, True, False]
}
df = pd.DataFrame(data)
# 筛出：有货（in_stock 为 True）、价格低于 3.0、且名字长度超过 4 个字母的行，打印结果。

