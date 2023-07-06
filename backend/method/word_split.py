import pandas as pd
import jieba

# 读取原始csv文件
df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\data.csv', header=None, names=['command', 'label'])

# 对第一列的句子进行分词
df['command'] = df['command'].apply(lambda x: ' '.join(jieba.cut(x)))

# 将处理后的数据保存到新的csv文件中
df.to_csv('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\data2.csv', index=False)
