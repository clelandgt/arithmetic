# -*- coding: utf-8 -*-
# @File  : find_the_duplicate_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :
from typing import List


class Solution1:
    """暴力破解，超时"""
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


def main():
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.findDuplicate(test_case))




if __name__ == '__main__':
    main()

