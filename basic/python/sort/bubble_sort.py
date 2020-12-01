# -*- coding: utf-8 -*-
# @File  : bubble_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 冒泡


def bubble_sort1(nums):
    """ 基于循环实现
    O(n^2)
    每次比较如果发现较小的元素在后面，就交换两个相邻的元素。排序序列顺序从左到右是从小到大，伪代码：
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums))[::-1]:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


def bubble_sort2(nums):
    """基于递归实现
    O(n^2)
    """
    def _bubble_sort2(nums, n):
        if n == len(nums):
            return

        for i in range(n, len(nums))[::-1]:
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        _bubble_sort2(nums, n + 1)

    _bubble_sort2(nums, 0)
    return nums


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    print('Solution1')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = bubble_sort1(test_case)
        print('after sort:', result)

    print('\nSolution2')
    for test_case in test_cases:
        print('before sort:', test_case)
        result = bubble_sort2(test_case)
        print('after sort:', result)


if __name__ == '__main__':
    main()
