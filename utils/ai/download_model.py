# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/13 10:58
@description  下载模型

参考资料：https://github.com/THUDM/ChatGLM3/blob/main/finetune_demo/README.md
安装依赖
pip install modelscope
缓存目录
~/.cache/huggingface
"""

from modelscope import AutoTokenizer, AutoModel, snapshot_download


def demo():
    """下载模型"""
    model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision="v1.0.0")


if __name__ == '__main__':
    demo()
