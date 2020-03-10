# -*- coding: utf-8 -*-
# @File  : calc_sort_degree.py
# @Author: clelandgt@163.com
# @Date  : 2019-10-30
# @Desc  : https://time.geekbang.org/column/article/73503
"""
问题：假设我们有 n 个数据，我们期望数据从小到大排列，那完全有序的数据的有序度就是 n(n-1)/2，逆序度等于 0；
     相反，倒序排列的数据的有序度就是 0，逆序度是 n(n-1)/2。除了这两种极端情况外，我们通过计算有序对或者
     逆序对的个数，来表示数据的有序度或逆序度。
eg:  2,4,3,1,5,6 逆序个数为4：(2,1) (4,3) (4,1) (3,1)
"""


def calc_sort_degree1(nums):
    """ 暴力求解直接遍历 """
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                result += 1
    return result


def main():
    nums = [2, 4, 3, 1, 5, 6]
    print("sort degree: ", calc_sort_degree1(nums))


if __name__ == '__main__':
    main()
