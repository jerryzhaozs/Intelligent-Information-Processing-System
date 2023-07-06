import pickle
from sklearn.feature_extraction.text import CountVectorizer
import jieba
# 从文件中加载分类器
def identify(content):
    if '异或' in content:
        return 6.7
    if '或' in content:
        return 6.5
    if '非' in content:
        return 6.6
    if '与' in content:
        return 6.4
    content=' '.join(jieba.cut(content))
    vectorizer = CountVectorizer()
    with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\classifier.pkl', 'rb') as f:
        classifier = pickle.load(f)
    with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\method\\vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    new_command = [content]
    new_command_features = vectorizer.transform(new_command)
    prediction = classifier.predict(new_command_features)
    return prediction[0]
