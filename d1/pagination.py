"""

    Pagination

"""


  # 1. 用 while 循环自动翻页，把 jsonplaceholder.typicode.com/posts 的所有数据全部拿到，打印每次拿了几条，最后打印总计几条。
import requests

all_data = []
start = 0

while True:
    params = {"_limit": 10, "_start": start}
    resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    data = resp.json()
    
    print(f"_start={start}，拿到 {len(data)} 条")
    
    if len(data) == 0 or len(data) < 10:
        break
    
    all_data.extend(data)
    start += 10

print(f"\n总计拿到：{len(all_data)} 条")

