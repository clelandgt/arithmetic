# -*- coding: utf-8 -*-
# @File  : binary_search_variety.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-31
# @Desc  :


def binary_search1(nums, num):
    print(nums)
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if num < nums[mid]:
            right = mid - 1
        elif num > nums[mid]:
            left = mid + 1
        else:
            if mid == 0 or num != nums[mid-1]:
                return mid
            else:
                right = mid - 1


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



if __name__ == '__main__':
    main()
