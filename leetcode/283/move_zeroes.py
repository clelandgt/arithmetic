# -*- coding: utf-8 -*-
# @File  : move_zeroes.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-01
# @Desc  :
from typing import List


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: 1 if x == 0 else 0)


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        not_null_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[not_null_index], nums[i] = nums[i], nums[not_null_index]
                not_null_index += 1


def main():
    test_cases = [
        [0, 1, 0, 3, 12]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        s1.moveZeroes(test_case)
        print(test_case)

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        s2.moveZeroes(test_case)
        print(test_case)


if __name__ == '__main__':
    main()

