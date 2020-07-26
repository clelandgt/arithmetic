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


class Solution2:
    """循环"""
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        nums_len = len(nums)
        left, right = 0, nums_len - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


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

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.search(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
