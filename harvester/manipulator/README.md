# manipulator
文本标注后台，提供前端接口

# 说明
1. 训练文本

文本数据的概念是以“文章”为单位，可以将其切为段落，段落可以切分为句子，句子可以切分为词

也就是说到words这里，应该是一个三维list；paragraph是二维list

# 搜狗新闻语料
链接: https://pan.baidu.com/s/1iaim_cNX8RBAc_hXWLDXIg 密码: asmp

# 文本分类
## 基于Sklearn
- [使用sklearn + jieba中文分词构建文本分类器](http://myg0u.com/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/2015/05/06/use-sklearn-jieba.html)

## 基于Tensorflow
### 使用神经网络
- [Understanding Convolutional Neural Networks for NLP](http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/)
- [CNN模型](http://www.jeyzhang.com/tensorflow-learning-notes-2.html)
- [利用TensorFlow实现卷积神经网络做文本分类](https://www.jianshu.com/p/ed3eac3dcb39)
- [Tensorflow实现CNN文本分类](https://www.jianshu.com/p/ff8e5f4635cc)
- [CNN与RNN中文文本分类-基于TensorFlow实现](https://gaussic.github.io/2017/08/30/text-classification-tensorflow/)
- [在TensorFlow中实现文本分类的卷积神经网络](http://www.tensorflownews.com/2017/08/21/implementing-a-cnn-for-text-classification-in-tensorflow/)

### 使用在线学习
- [tensorflow实现基于LSTM的文本分类方法](http://blog.csdn.net/u010223750/article/details/53334313)


# Word2Vec
- [implement word2vec embedding in tensorflow](https://towardsdatascience.com/learn-word2vec-by-implementing-it-in-tensorflow-45641adaf2ac)

# NER
- [当RNN神经网络遇上NER（命名实体识别）：双向LSTM，条件随机场（CRF），层叠Stack LSTM， 字母嵌入](http://nooverfit.com/wp/%E5%BD%93rnn%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E9%81%87%E4%B8%8Aner%EF%BC%88%E5%91%BD%E5%90%8D%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB%EF%BC%89%EF%BC%9A%E5%8F%8C%E5%90%91lstm%EF%BC%8C%E6%9D%A1%E4%BB%B6/)