# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/15 10:03
@description  解析 ckpt 文件 注：未实践成功

pip install tensorflow
"""

import tensorflow as tf


def demo():
    print(tf.__version__)


def demo1():
    # 创建一个 TensorFlow Session
    sess = tf.compat.v1.Session()

    # 加载 .ckpt 文件中的图结构和变量值
    saver = tf.compat.v1.train.import_meta_graph('path/to/model.ckpt.meta')
    saver.restore(sess, 'path/to/model.ckpt')

    # 获取图中的变量
    graph = tf.compat.v1.get_default_graph()
    var1 = graph.get_tensor_by_name('variable_name:0')  # 根据变量名获取张量

    # 使用 Session 获取变量的值
    var1_value = sess.run(var1)
    print(var1_value)

    # 关闭 Session
    sess.close()


if __name__ == '__main__':
    demo()
