# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/16 14:52
@description
"""

import gradio as gr


def greet(name):
    return "Hello " + name


if __name__ == '__main__':
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()
