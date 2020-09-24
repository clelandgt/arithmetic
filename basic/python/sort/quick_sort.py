# -*- coding: utf-8 -*-
# @File  : quick_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 快速排序 https://time.geekbang.org/column/article/41913


def quick_sort(nums):
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
        return nums

    return _quick_sort(nums, 0, len(nums)-1)


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    for test_case in test_cases:
        print('before sort:', test_case)
        print('after sort:', quick_sort(test_case))


if __name__ == '__main__':
    main()
