# 题1
# 元组拆包遍历，打印每条：abc123 来自 r/mentalhealth
records = [("abc123", "mentalhealth"), ("xyz999", "depression"), ("def456", "Anxiety")]



# 题2：
texts = ["I talked to ChatGPT today", "Feeling sad", "Claude really helped me", "I don't know"]
# 过滤掉不足5词的，剩下的检查有没有 "chatgpt" 或 "claude"，打印结果。

# 题3：
posts = [
    ("abc123", "mentalhealth", "  I talked to ChatGPT and it really helped me feel better  "),
    ("xyz999", "depression", None),
    ("def456", "Anxiety", "  Feeling very sad today  "),
    ("ghi789", "therapy", "  Claude helped me process my trauma and anxiety  "),
]
# 元组拆包遍历，跳过 None，转小写去空格，不足6词跳过，把结果存进 DataFrame，列名 post_id、words、has_ai，保存成 results.csv。最后用 f-string 打印含AI比例（:.1%）。

