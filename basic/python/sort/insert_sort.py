# -*- coding: utf-8 -*-
# @File  : insert_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 插入排序
"""
已排序的[0, n-1]加入n后再排序。
"""
from copy import deepcopy


def insert_sort1(nums):
    """循环
    时间复杂度: O(n^2)
    """
    for i in range(len(nums)):
        for j in range(1, i+1)[::-1]:
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
    return nums


def insert_sort2(nums):
    """递归
    时间复杂度: O(n^2)
    """
    def _insert_sort2(nums, n):
        if n == len(nums):
            return
        for i in range(1, n+1)[::-1]:
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                break
        _insert_sort2(nums, n+1)
    _insert_sort2(nums, 1)
    return nums


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    print('Solution1')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = insert_sort1(deepcopy(test_case))
        print('after sort:', result)

    print('\nSolution2')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = insert_sort2(deepcopy(test_case))
        print('after sort:', result)


if __name__ == '__main__':
    main()
