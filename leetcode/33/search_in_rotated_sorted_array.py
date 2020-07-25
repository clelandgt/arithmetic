# -*- coding: utf-8 -*-
# @File  : search_in_rotated_sorted_array.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-25
# @Desc  :
from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        """递归"""
        if nums is None or len(nums) == 0:
            return -1
        nums_len = len(nums)

        def _search(nums, left, right, target):
            if left > right:
                return -1

            mid = int((right + left) / 2)
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return _search(nums, left, mid-1, target)
                else:
                    return _search(nums, mid+1, right, target)

            else:
                if nums[mid] <= target <= nums[right]:
                    return _search(nums, mid+1, right, target)
                else:
                    return _search(nums, left, mid-1, target)

        return _search(nums, 0, nums_len-1, target)


def main():
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([3, 5, 1], 3),
        ([5, 1, 3], 3)

    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.search(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
