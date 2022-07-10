# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/8/23 11:45
@description  情感分析，借助情感分析 pipeline，只需要输入文本，就可以得到其情感标签（积极/消极）以及对应的概率
参考资料：https://transformers.run/intro/2021-12-08-transformers-note-1/
        https://huggingface.co/gpt2
"""

from transformers import pipeline


def sentiment():
    classifier = pipeline("sentiment-analysis")
    result = classifier("I've been waiting for a HuggingFace course my whole life.")
    print(result)

    results = classifier(
        ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!", "bad", "happy"]
    )
    print(results)


# 文本生成：首先根据任务需要构建一个模板 (prompt)，然后将其送入到模型中来生成后续文本。注意，由于文本生成具有随机性，因此每次运行都会得到不同的结果。
def text():
    generator = pipeline("text-generation")
    results = generator("I am a actor")
    print(results)

    results = generator(
        "I am a actor",
        num_return_sequences=2,
        max_length=50
    )
    print(results)


def text2():
    generator = pipeline("text-generation", model="uer/gpt2-chinese-poem")
    results = generator(
        "[CLS] 星期天，",
        num_return_sequences=2,
        max_length=50
    )
    print(results)


if __name__ == '__main__':
    # sentiment()
    # text()
    text2()
