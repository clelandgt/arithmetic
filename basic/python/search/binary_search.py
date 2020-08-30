# -*- coding: utf-8 -*-
# @File  : binary_search.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-04
# @Desc  : 二分搜索。https://time.geekbang.org/column/article/42520


def binary_search(nums, num):
    return _binary_search(nums, num, left=0, right=len(nums)-1)


def _binary_search(nums, num, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    if nums[middle] == num:
        return middle
    elif nums[middle] > num:
        return _binary_search(nums, num, left, middle-1)
    else:
        return _binary_search(nums, num, middle+1, right)


def main():
    test_cases = [
        [[1, 2, 3, 7, 9, 10, 21, 100, 120, 130, 131, 140], 10]
    ]
    for test_case in test_cases:
        index = binary_search(test_case[0], test_case[1])
        print('nums: ', test_case[0])
        print('search: ', test_case[1])
        print('index: ', index)


if __name__ == '__main__':
    main()
