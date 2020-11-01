# -*- coding: utf-8 -*-
# @File  : sort_colors.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-18
# @Desc  :
from typing import List
from copy import deepcopy


class Solution1:
    """计数排序
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
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


class Solution2:
    """单指针 两次遍历
    1. 迭代遍历, 把0放到数组之首；
    2. 迭代遍历, 把1放到0之后；
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1

        for i in range(count, len(nums)):
            if nums[i] == 1:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1

        return nums


class Solution3:
    """双指针 一次遍历
    参考：https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        if size < 2:
            return
        i, zero, two = 0, 0, size-1
        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1

        return nums


def main():
    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [1, 2, 0]
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s1.sortColors(test_case)
        print(test_case)

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s2.sortColors(test_case)
        print(test_case)

    print('Solution3')
    s3 = Solution3()
    for test_case in test_cases:
        test_case = deepcopy(test_case)
        s3.sortColors(test_case)
        print(test_case)


if __name__ == '__main__':
    main()
