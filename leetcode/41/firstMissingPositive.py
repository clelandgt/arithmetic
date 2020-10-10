# -*- coding: utf-8 -*-
# @File  : firstMissingPositive.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-10
# @Desc  : https://leetcode-cn.com/problems/first-missing-positive/


class Solution1:
    """ 使用哈希表
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def firstMissingPositive(self, nums):
        value_counts = {}
        for i in range(len(nums)+1):
            value_counts[i+1] = 0
        for item in nums:
            if item <= 0:
                continue
            if item not in value_counts:
                value_counts[item] = 1
            else:
                value_counts[item] += 1
        for item in value_counts.items():
            if item[1] == 0:
                return item[0]


class Solution2:
    """ 使用哈希表
    优化后
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def firstMissingPositive(self, nums):
        value_dict = {k: 0 for k in nums if k > 0}
        for i in range(1, len(nums)+2):
            if i not in value_dict:
                return i


def main():
    test_cases = [
        [],
        [1],
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.firstMissingPositive(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.firstMissingPositive(test_case))


if __name__ == '__main__':
    main()
