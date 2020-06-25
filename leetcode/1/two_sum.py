# -*- coding: utf-8 -*-
# @File  : two_sum.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-20
# @Desc  : https://leetcode.com/problems/two-sum/
from typing import List


class Solution1:
    """ 两层遍历，暴力求解(Brute Force)
     Time: O(n^2)  Space: O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


class Solution2:
    """ 一个哈希表+单次数组遍历
    哈希表的对应的key=target-item(遍历nums的元素), value=item对应的下标
    Time: O(n)  Space: O(n)
    """

    def _twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """version1
        改进点：1. len(nums)<=1 未做处理；2. 不需单独遍历一次生成哈希表
        """
        nums_dict = {}
        for i, item in enumerate(nums):
            nums_dict[item] = i

        for i, item in enumerate(nums):
            j = target - item
            if nums_dict.get(j) is not None and i != nums_dict.get(j):
                return i, nums_dict[j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            False

        tmp_dict = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in tmp_dict.keys():
                return tmp_dict[remaining], i
            else:
                tmp_dict[v] = i


def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution2()
    print(s.twoSum(nums, target))


if __name__ == '__main__':
    main()
