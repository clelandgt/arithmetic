# -*- coding: utf-8 -*-
# @File  : get_max_permutation.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-11
# @Desc  : [Python算法教程][第4章 归纳、递归与规归简][基于归纳法(与递归法)的设计][4.4.1寻找最大排列]
#          解题思路图片连接：1. https://cleland.oss-cn-beijing.aliyuncs.com/arithmetic/python%E7%AE%97%E6%B3%95%E6%95%99%E7%A8%8B/4-5/4.4.1_1.jpeg
#                          2. https://cleland.oss-cn-beijing.aliyuncs.com/arithmetic/python%E7%AE%97%E6%B3%95%E6%95%99%E7%A8%8B/4-5/4.4.1_1.jpeg


def get_max_permutation1(nums, remain_index=[]):
    if not remain_index:
        remain_index = list(range(len(nums)))
    if len(remain_index) == 1:
        return remain_index
    remain_value = [nums[item] for item in remain_index]
    diff = set(remain_index) - set(remain_value)
    if len(diff) == 0:
        return remain_index
    else:
        remain_index.remove(diff.pop())
        return get_max_permutation1(nums, remain_index)


def main():
    nums = [2, 2, 0, 5, 3, 5, 7, 4]
    print(get_max_permutation1(nums))


if __name__ == '__main__':
    main()