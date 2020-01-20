# -*- coding: utf-8 -*-
# @File  : single_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-21
# @Desc  : https://leetcode.com/problems/single-number/
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return False
        elif len(nums) == 1:
            return nums[0]

        result = []
        for item in nums:
            if item not in result:
                result.append(item)
            else:
                result.remove(item)
        return result.pop()


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return False
        elif len(nums) == 1:
            return nums[0]

        tmp_dict = {}
        for item in nums:
            if item not in tmp_dict.keys():
                tmp_dict[item] = 1
            else:
                tmp_dict.pop(item)
        return tmp_dict.popitem()[0]


def main():
    # Input: [4,1,2,1,2], Output: 4
    nums = [4, 1, 2, 1, 2]
    s = Solution2()
    print(s.singleNumber(nums))


if __name__ == '__main__':
    main()
