# -*- coding: utf-8 -*-
# @File  : find_first_and_last_position_of_element_in_sorted_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-26
# @Desc  :
from typing import List


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]


def main():
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6)
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.searchRange(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()

