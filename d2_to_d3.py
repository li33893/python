import requests
import pandas as pd
import json
import re
import time

API_KEY = "你的key放这里"

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