import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
# 读取文本文件
with open('baogao.txt', 'r', encoding='utf-8') as f:
    text = f.read()


# 提取主题和关键词
tags = jieba.analyse.extract_tags(text, topK=100, withWeight=True, allowPOS=('n', 'vn', 'v'))

# 绘制词云图
wordcloud = WordCloud(width=800, height=600, background_color='white', font_path='msyh.ttc')
keywords = dict(tags)
wordcloud.generate_from_frequencies(keywords)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

以下内容是不选择关键词的词云图
## 对文本进行分词
words = jieba.cut(text)

# 将分词结果转化为字符串
text = ' '.join(words)

# 生成词云图
wordcloud = WordCloud(background_color='white', width=800, height=600, font_path='simhei.ttf').generate(text)

# 显示词云图
plt.imshow(wordcloud)
plt.axis('off')
plt.show()