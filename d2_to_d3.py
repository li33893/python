import requests
import pandas as pd
import json
import re
import time

posts = [
    {"id": "001", "title": "ChatGPT saved me", "body": "I was feeling so alone last night and I opened ChatGPT and just started talking. It actually helped me calm down."},
    {"id": "002", "title": "Feeling anxious today", "body": "I don't know why but I can't stop shaking. Everything feels wrong."},
    {"id": "003", "title": "AI tools for therapy", "body": "Has anyone used AI-powered tools for mental health support? I've been using one for a month."},
]

# 模拟API返回的筛查结果（正常的）
api_responses = [
    '{"relevant": true, "confidence": 0.9, "risk_level": 1, "reason": "user describes personal AI interaction"}',
    '{"relevant": false, "confidence": 0.8, "risk_level": 1, "reason": "no AI mention"}',
    '{"relevant": true, confidence: 0.7, "risk_level": 1, "reason": "user asks about AI tools"}',  # 故意坏掉的
]

# 用re.compile()过滤帖子，只保留title+body合并后包含\bai\b或ai-的
# 每篇之间time.sleep(0.5)
# 过滤后的帖子用f-string打印：Post {id}: {title}
# 用try/except逐条解析api_responses，成功就打印relevant和reason，失败就打印f"解析失败：{type(e).__name__}：{e}"
# 把过滤后的帖子存成DataFrame，列名id、title、body，保存成filtered_posts.csv