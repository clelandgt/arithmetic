# -*- coding: utf-8 -*-
# @File  : quick_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 快速排序 https://time.geekbang.org/column/article/41913


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums.pop()
    greater, lesser = [], []
    for num in nums:
        if num > pivot:
            greater.append(num)
        else:
            lesser.append(num)

    return lesser + [pivot] + greater


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    for test_case in test_cases:
        print('before sort:', test_case)
        print('after sort:', quick_sort(test_case))


if __name__ == '__main__':
    main()
