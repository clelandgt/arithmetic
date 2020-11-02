# -*- coding: utf-8 -*-
# @File  : remove_element.py
# @Author: clelandgt@163.com
# @Date  : 2020-11-02
# @Desc  :
from typing import List


class Solution1:
    """双指针
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        slow, fast = -1, 0
        while fast < size:
            if nums[fast] == val:
                pass
            else:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1


def main():
    test_cases = [
        [[3, 2, 2, 3], 3],
        [[0, 1, 2, 2, 3, 0, 4, 2], 2]
    ]

    s1 = Solution1()
    print('Solution1')
    for test_case in test_cases:
        print(s1.removeElement(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
