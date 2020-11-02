# -*- coding: utf-8 -*-
# @File  : quick_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 快速排序 https://time.geekbang.org/column/article/41913
# 参考： https://www.jb51.net/article/158963.htm


def quick_sort1(nums):
    """ 快速排序1
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    :param nums:
    :return:
    """
    def _quick_sort(nums, start, end):
        if start >= end:
            return
        p = nums[start]
        i = start
        j = end
        while i < j:
            while i < j and nums[j] >= p:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= p:
                i += 1
            nums[j] = nums[i]

        nums[j] = p
        _quick_sort(nums, start, i-1)
        _quick_sort(nums, i+1, end)

    _quick_sort(nums, 0, len(nums)-1)


def quick_sort2(nums):
    """ 快速排序2: 只用了一层循环，并且一趟就完成分片

    时间复杂度: O(n^2)
    空间复杂度: O(1)
    :param nums:
    :return:
    """
    def _quick_sort(nums, start, end):
        if start >= end:
            return
        p = partition(nums, start, end)
        _quick_sort(nums, start, p-1)
        _quick_sort(nums, p+1, end)

    def partition(nums, start, end):
        """双指针"""
        piovt = nums[end]
        less_index = start - 1
        for i in range(start, end):
            if nums[i] <= piovt:
                less_index += 1
                nums[i], nums[less_index] = nums[less_index], nums[i]
        less_index += 1
        nums[less_index], nums[end] = nums[end], nums[less_index]
        return less_index

    _quick_sort(nums, 0, len(nums)-1)


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    print("quick sort1")
    for test_case in test_cases:
        print('before sort:', test_case)
        quick_sort1(test_case)
        print('after sort:', test_case)

    print("quick sort2")
    for test_case in test_cases:
        print('before sort:', test_case)
        quick_sort2(test_case)
        print('after sort:', test_case)

if __name__ == '__main__':
    main()
