# -*- coding: utf-8 -*-
# @File  : find_the_duplicate_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  : 解决方案：https://leetcode.com/problems/find-the-duplicate-number/discuss/705111/summary-7-solutions-%2B-consice-explanation-and-complexity-analysis
from typing import List


class Solution1:
    """暴力破解，超时
    时间复杂度: O(n^2)
    空间复杂度: O(n)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


class Solution2:
    """ 二分搜索
    时间复杂度: O(nlogn)
    空间复杂度: O(1)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums)-1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            less, equal = 0, 0
            for num in nums:
                if num < mid:
                    less += 1
                if num == mid:
                    equal += 1
            if equal >= 2:
                return mid
            if less >= mid:
                hi = mid - 1
            else:
                lo = mid + 1


class Solution3:
    """哈希
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if result.get(num):
                return num
            else:
                result[num] = 1
        return -1


def main():
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.findDuplicate(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.findDuplicate(test_case))

    print('Solution3')
    s3 = Solution3()
    for test_case in test_cases:
        print(s3.findDuplicate(test_case))


if __name__ == '__main__':
    main()
