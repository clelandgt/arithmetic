# -*- coding: utf-8 -*-
# @File  : binary_search_variety4.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-31
# @Desc  : 查找最后一个小于等于给定值的元素


def binary_search1(nums, num):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > num:
            right = mid - 1
        else:
            if mid == len(nums)-1 or nums[mid+1] > num:
                return mid
            else:
                left = mid + 1

    return -1


def main():
    test_cases = [
        [[1, 3, 4, 5, 6, 8, 8, 8, 11, 18], 8]
    ]
    for test_case in test_cases:
        print('binary_search1')
        index = binary_search1(test_case[0], test_case[1])
        print('nums: ', test_case[0])
        print('search: ', test_case[1])
        print('index: ', index)


if __name__:
    main()
