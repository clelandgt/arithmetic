# -*- coding: utf-8 -*-
# @File  : sort_colors.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-18
# @Desc  :
from typing import List


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        values_count = {
            '0': 0,
            '1': 0,
            '2': 0
        }
        for num in nums:
            values_count[str(num)] += 1

        result = [0] * values_count['0'] + [1] * values_count['1'] + [2] * values_count['2']
        for index, item in enumerate(nums):
            nums[index] = result[index]


def main():
    test_cases = [
        [2, 0, 2, 1, 1, 0]
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        s1.sortColors(test_case)
        print(test_case)


if __name__ == '__main__':
    main()
