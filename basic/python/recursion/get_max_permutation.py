# -*- coding: utf-8 -*-
# @File  : get_max_permutation.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-11
# @Desc  : [Python算法教程][第4章 归纳、递归与规归简][基于归纳法(与递归法)的设计][4.4.1寻找最大排列]
#          解题思路图片连接：


def get_max_permutation1(nums, remain_index=[]):
    if not remain_index:
        remain_index = list(range(len(nums)))

    diff = set(remain_index) - set([nums[item] for item in remain_index])
    if len(diff) == 0:
        return
    else:
        remain_index.remove(diff.pop())
        get_max_permutation1(nums, remain_index)
        return set(nums)


def main():
    nums = [2, 2, 0, 5, 3, 5, 7, 4]
    print(get_max_permutation1(nums))


if __name__ == '__main__':
    main()