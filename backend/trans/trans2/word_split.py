import thulac

# 加载模型
thu = thulac.thulac(seg_only=True)


# 分词
text = "这是一段没有标点符号的中文文本我想要将其分成多个句子"
result = thu.cut(text)

# 分句
sentences = []
sentence = ""
for word in result:
    sentence += word[0]
    if "。" in word[0]:
        sentences.append(sentence)
        sentence = ""

print(sentences)