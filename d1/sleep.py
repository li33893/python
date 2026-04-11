"""

    time.sleep()
    你发请求太快，服务器会觉得你在攻击它，然后把你封掉。time.sleep() 就是让程序等一会儿再继续。

"""


import requests
import time

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
    time.sleep(0.5)    # 每次请求后等0.5秒

print(f"\n总计拿到：{len(all_data)} 条")