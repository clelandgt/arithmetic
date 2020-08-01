# -*- coding: utf-8 -*-
# @File  : majority_element.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :
from typing import List


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        value_counts = {}
        size = len(nums)

        for num in nums:
            if num not in value_counts:
                value_counts[num] = 1
            else:
                value_counts[num] += 1
            if value_counts[num] > int(size/2):
                return value_counts[num]


def main():
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.majorityElement(test_case))


if __name__ == '__main__':
    main()
