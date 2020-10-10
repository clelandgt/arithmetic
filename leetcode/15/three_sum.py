# -*- coding: utf-8 -*-
# @File  : three_sum.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-10
# @Desc  : https://leetcode-cn.com/problems/3sum/


class Solution1:
    """暴力求解(超时)
    时间复杂度：O(n^3)
    空间复杂度：O(1)
    """
    def threeSum(self, nums):
        result = {}
        nums = sorted(nums, key=lambda item: item)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for z in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[z] == 0:
                        key = hash(str(nums[i]) + str(nums[j]) + str(nums[z]))
                        if key not in result:
                            result[key] = [nums[i], nums[j], nums[z]]

        return list(result.values())


def main():
    test_cases = [
        (0, 0, 0, 0, 0, 0),
        (-1, 0, 1, 2, -1, -4)
    ]

    s1 = Solution1()
    for test_case in test_cases:
        print(s1.threeSum(test_case))


if __name__ == '__main__':
    main()
