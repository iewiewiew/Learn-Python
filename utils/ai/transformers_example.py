# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/8/23 11:33
@description  transformers 例子

参考资料：https://huggingface.co/THUDM/chatglm-6b
pip install transformers torch torchvision torchaudio
pip install protobuf==3.20.0 transformers==4.27.1 icetk cpm_kernels
"""


def demo1():
    from transformers import BertTokenizer, BertForSequenceClassification

    # 加载预训练的BERT模型和tokenizer
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)

    # 准备文本输入
    text = "This is an example sentence."
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    # 运行模型进行文本分类
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()

    # 打印结果
    print("输入文本:", text)
    print("预测的类别:", predicted_class)


if __name__ == '__main__':
    demo1()
