# -*- coding: utf-8 -*-
# @File  : insert_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 插入排序
"""
已排序的[0, n-1]加入n后再排序。
"""


def insert_sort1(nums):
    """循环"""
    for i in range(len(nums)):
        for j in range(1, i+1)[::-1]:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]

    return nums


def insert_sort2(nums):
    """递归"""

    def _insert_sort2(nums, n):
        if n == 0:
            return
        _insert_sort2(nums, n-1)
        for i in range(1, n)[::-1]:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    _insert_sort2(nums, len(nums))

    return nums


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    print('Solution1')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = insert_sort1(test_case)
        print('after sort:', result)

    print('Solution2')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = insert_sort2(test_case)
        print('after sort:', result)


if __name__ == '__main__':
    main()
