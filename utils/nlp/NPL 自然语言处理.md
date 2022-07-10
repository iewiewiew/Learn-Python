[TOC]

<h1 align="center">NPL 自然语言处理</h1>

> By：weimenghua  
> Date：2023.08.23  
> Description：  

**参考资料**
[HuggingFace 官网](https://huggingface.co/)  
[HuggingFace Github](https://github.com/huggingface)
[HuggingFace 在线教程](https://huggingface.co/learn/nlp-course/chapter1/1)  
[OpenAI](https://openai.com/)



### 一、HuggingFace

Datasets：数据集，以及数据集的下载地址
Models：包括各种处理 CV 和 NLP 等任务的模型，主要包括计算机视觉、自然语言处理、语音处理、多模态、表格处理、强化学习
course：nlp 课程
docs：文档



### 二、Transformers

[Transformers 是由 Hugging Face 开发的一个 NLP 包](https://transformers.run/)，详细可查看 [Transformers 简介](https://huggingface.co/docs/transformers/v4.27.2/zh/index) 、[Transformers 官方文档](https://huggingface.co/docs/transformers/index) 。

Transformers 库将目前的 NLP 任务归纳为几下几类：
- 文本分类：例如情感分析、句子对关系判断等；
- 对文本中的词语进行分类：例如词性标注 (POS)、命名实体识别 (NER) 等；
- 文本生成：例如填充预设的模板 (prompt)、预测文本中被遮掩掉 (masked) 的词语；
- 从文本中抽取答案：例如根据给定的问题从一段文本中抽取出对应的答案；
- 根据输入文本生成新的句子：例如文本翻译、自动摘要等。

pipeline 函数，它支持如下的任务：
- 情感分析(Sentiment analysis)：一段文本是正面还是负面的情感倾向
- 文本生成(Text generation)：给定一段文本，让模型补充后面的内容
- 命名实体识别(Name entity recognition)：识别文字中出现的人名地名的命名实体
- 问答(Question answering)：给定一段文本以及针对它的一个问题，从文本中抽取答案
- 填词(Filling masked text)：把一段文字的某些部分mask住，然后让模型填空
- 摘要(Summarization)：根据一段长文本中生成简短的摘要
- 翻译(Translation)：把一种语言的文字翻译成另一种语言
- 特征提取(Feature extraction)：把一段文字用一个向量来表示



### 三、使用教程

安装依赖
```
# 安装基础版
pip install datasets
# 安装for声音
pip install datasets[audio]
# 安装for图像
pip install datasets[vision]
```