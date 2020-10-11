# -*- coding: utf-8 -*-
# @File  : max_sliding_window.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :
from typing import List


class Solution1:
    """ 暴力破解(超时)
    时间复杂度：O(n^2)
    空间复杂度：O(n)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) < k:
            return result
        for i in range(k-1, len(nums)):
            result.append(max(nums[i-k+1: i+1]))
        return result


def main():
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3)
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.maxSlidingWindow(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
