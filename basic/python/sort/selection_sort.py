# -*- coding: utf-8 -*-
# @File  : selection_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 选择排序
"""
冒泡算法，每次比较如果发现较小的元素在后面，就交换两个相邻的元素。而选择排序算法的改进在于得到所谓的最小值时再做交换
序列顺序从左到右是从小到大，伪代码：
for i in [0, n):
    min_index = i
    for j in (i, n-1]:
        if l[j] < l[min_index]:
            min_index = j
    swap(l[i], l[min_index])
"""


def selection_sort1(nums):
    """基于循环"""
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def selection_sort2(nums):
    """递归"""
    def _selection_sorts(nums, n):
        if n == len(nums):
            return
        min_index = n
        for i in range(n, len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[n], nums[min_index] = nums[min_index], nums[n]
    _selection_sorts(nums, 0)

    return nums


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    print('Solution1')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = selection_sort1(test_case)
        print('after sort:', result)

    print('Solution2')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = selection_sort2(test_case)
        print('after sort:', result)


if __name__ == '__main__':
    main()
