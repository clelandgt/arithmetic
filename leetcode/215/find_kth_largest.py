# -*- coding: utf-8 -*-
# @File  : find_kth_largest.py
# @Author: clelandgt@163.com
# @Date  : 2020-11-02
# @Desc  : 数组中的第K个最大元素

from typing import List


class Solution1:
    """选择排序 暴力求解
    时间复杂度: O(n^2)
    空间复杂度: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        if k > size:
            return

        for i in range(k):
            max_index = i
            for j in range(i+1, size):
                if nums[j] > nums[max_index]:
                    max_index = j
            nums[i], nums[max_index] = nums[max_index], nums[i]
        return nums[k-1]


def main():
    test_cases = [
        [[3, 2, 1, 5, 6, 4], 2],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.findKthLargest(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
