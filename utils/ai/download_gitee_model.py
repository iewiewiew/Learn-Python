# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/12/22 10:22
@description  下载 GiteeAI 模型
"""

"""
// 执行上面脚本时，请设置环境变量：
export HF_ENDPOINT=https://ai.gitee.com/huggingface
export HF_HOME=~/.cache/gitee-ai

echo $HF_ENDPOINT
echo $HF_HOME
"""


def demo1():
    from datasets import load_dataset
    dataset = load_dataset("iewiewiew/wei-dataset-001")


def demo2():
    from datasets import load_dataset
    dataset = load_dataset("lavita/medical-qa-shared-task-v1-toy")


def demo3():
    from datasets import load_dataset
    dataset = load_dataset("PKU-Alignment/PKU-SafeRLHF")


if __name__ == '__main__':
    demo1()
    demo2()
    demo3()