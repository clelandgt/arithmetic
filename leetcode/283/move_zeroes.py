# -*- coding: utf-8 -*-
# @File  : move_zeroes.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-01
# @Desc  :
from typing import List


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: 1 if x == 0 else 0)


def main():
    test_cases = [
        [0, 1, 0, 3, 12]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        s1.moveZeroes(test_case)
        print(test_case)


if __name__ == '__main__':
    main()

