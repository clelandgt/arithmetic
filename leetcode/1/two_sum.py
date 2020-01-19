# -*- coding: utf-8 -*-
# @File  : two_sum.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-20
# @Desc  : https://leetcode.com/problems/two-sum/
from typing import List


class Solution1:
    """ 两次遍历，暴力求解 """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=1:
            return False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j



def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution1()
    print(s.twoSum(nums, target))


if __name__ == '__main__':
    main()
