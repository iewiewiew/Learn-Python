# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/12/1 11:27
@description
"""


def text_generation_example():
    from transformers import pipeline
    text_generator = pipeline("text-generation")
    print(text_generator("As far as I am concerned, I will", max_length=50, do_sample=False))


if __name__ == '__main__':
    text_generation_example()
