# -*- coding: utf-8 -*-
# @File  : longest_increasing_subsequence.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :
from typing import  List


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


def main():
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.lengthOfLIS(test_case))


if __name__ == '__main__':
    main()

