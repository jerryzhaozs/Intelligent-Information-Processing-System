import pandas as pd
import jieba

# 读取原始csv文件
df = pd.read_csv('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\data.csv', header=None, names=['command', 'label'])

# 对第一列的句子进行分词
df['command'] = df['command'].apply(lambda x: ' '.join(jieba.cut(x)))

# 将处理后的数据保存到新的csv文件中
df.to_csv('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\data2.csv', index=False)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# 读取CSV文件
data = pd.read_csv('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\data2.csv', header=None, names=['command', 'label'])

# 将输入数据转换成特征向量
X = data['command']
y = data['label']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001,random_state=34)

# 创建特征提取器并对训练集进行拟合
vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)

# 创建分类器并训练模型
classifier = LogisticRegression()
classifier.fit(X_train_features, y_train)

# 在测试集上进行预测
X_test_features = vectorizer.transform(X_test)
y_pred = classifier.predict(X_test_features)

# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print('train_input Done')

# 对新指令进行特征提取并使用模型进行预测
# new_command = ['删除历史']
# new_command_features = vectorizer.transform(new_command)
# prediction = classifier.predict(new_command_features)
# print(prediction[0])

import pickle

# 假设分类器对象为classifier
with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)
with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
