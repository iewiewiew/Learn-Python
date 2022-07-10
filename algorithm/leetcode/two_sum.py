# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/8/9 22:14
@description  两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是数组中同一个元素在答案里不能重复出现。

示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""

from typing import List


def demo(nums: List[int], target: int) -> List[int]:
    helper = {}
    for i, v in enumerate(nums):
        num = target - v
        if num in helper:
            return [helper[num], i]
        helper[v] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(demo(nums, target))

