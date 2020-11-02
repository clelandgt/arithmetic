# -*- coding: utf-8 -*-
# @File  : remove_duplicates.py
# @Author: clelandgt@163.com
# @Date  : 2020-11-02
# @Desc  :
from typing import List


class Solution1:
    """ 循环不变量
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                del nums[index]
            else:
                index += 1

        return len(nums)


class Solution2:
    """ 双指针
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        slow, fast = 0, 1
        while fast < size:
            if nums[fast] == nums[fast-1]:
                pass
            else:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


def main():
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.removeDuplicates(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.removeDuplicates(test_case))


if __name__ == '__main__':
    main()
