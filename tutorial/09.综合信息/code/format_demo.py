#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2020/11/1 8:55
@description 格式化输出
"""


# 总占位50个字符空间，不足部分以“-”来填充
# 居中显示，且有千位分隔符
# 小数部分只保留2位，还进行了四舍五入
# 最终返回浮点数的类型
def demo():
    a = 123456.7890
    print("{0:-^50,.5f}".format(a))
    print('{} 和 {}'.format("张三", "李四"))
    print('姓名：{name}  职业：{job}'.format(name='张艺兴', job='歌手'))


if __name__ == '__main__':
    demo()
