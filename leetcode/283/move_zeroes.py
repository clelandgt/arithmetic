# -*- coding: utf-8 -*-
# @File  : move_zeroes.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-01
# @Desc  :
from typing import List
from copy import copy, deepcopy


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: 1 if x == 0 else 0)


class Solution2:
    """双指针 正向
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        not_null_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[not_null_index], nums[i] = nums[i], nums[not_null_index]
                not_null_index += 1


class Solution3:
    """双指针 逆向 (错误)，因为要保持非0元素的位置不变
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        index, size, zero = 0, len(nums), len(nums)
        while index < zero:
            if nums[index] == 0:
                zero -= 1
                nums[index], nums[zero] = nums[zero], nums[index]
            index += 1
        return nums


def main():
    test_cases = [
        [0, 1, 0, 3, 12]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s1.moveZeroes(test_case)
        print(test_case)

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s2.moveZeroes(test_case)
        print(test_case)

    print('Solution3')
    s3 = Solution3()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s3.moveZeroes(test_case)
        print(test_case)


if __name__ == '__main__':
    main()

