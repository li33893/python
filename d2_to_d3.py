import requests
import pandas as pd
import json
import re
import time

API_KEY = ""

SYSTEM_PROMPT = "You are a research assistant. Given a Reddit post, decide if the user describes a personal experience using an AI tool for emotional support. Respond ONLY with a JSON object: {\"relevant\": true or false, \"reason\": \"one sentence\"}"

posts = [
    {"id": "001", "title": "ChatGPT saved me", "body": "I was feeling so alone last night and I opened ChatGPT and just started talking. It actually helped me calm down."},
    {"id": "002", "title": "Feeling anxious today", "body": "I don't know why but I can't stop shaking. Everything feels wrong."},
    {"id": "003", "title": "AI tools for therapy", "body": "Has anyone used AI-powered tools for mental health support? I've been using one for a month."},
]

# 用re.compile()过滤，只保留title+body合并后包含\bai\b或ai-的帖子
# 每篇之间time.sleep(0.5)
# 过滤后的帖子用f-string打印：Post {id}: {title}
# 对每篇过滤后的帖子构造payload，用requests.post()发给Claude API，timeout=60
# 用try/except解析返回的JSON，成功打印relevant和reason，失败打印f"解析失败：{type(e).__name__}：{e}"
# 把所有结果存成DataFrame，列名id、title、relevant、reason，保存成results.csv

pattern = re.compile(r'\bai\b', re.IGNORECASE)
post_filtered = []
post_text = "Is this post relevant to AI mental health?"
SYSTEM_PROMPT = 'You are a helpful assistant. Respond ONLY with a JSON object: {"relevant": true or false, "reason": "one sentence"}'

for post in posts:
    text = f"{post["title"]}\n{post["body"]}"
    if pattern.search(text) is not None:
        time.sleep(0.5)
        print(f"post{post["id"]}:{post["title"]}")

        payload = {
            "model" : "claude-sonnet-4-20250514",
            "max_tokens" : 100,
            "system" : SYSTEM_PROMPT,
            "messages" : [
                {"role" : "user", "content" : post_text}
            ]
        }

        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "Content-Type": "application/json",
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01"
            },
            json=payload,
            timeout=60
        )

        try:
            resp_j = resp.json()["content"][0]["text"]
            result = json.loads(resp_j)
            print(result["relevant"])
            print(result["reason"])
            post_filtered.append({"id":post["id"],"title":post["title"],"body":post["body"],"relevant":result["relevant"],"reason":result["reason"]})
        except Exception as e:
            print(f"解析失败：{type(e).__name__}：{e}")
    
data = pd.DataFrame(post_filtered)
data.to_csv("results.csv", index = False, encoding="utf-8-sig")

        

        
        
        
    