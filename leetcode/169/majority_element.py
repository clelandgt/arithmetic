# -*- coding: utf-8 -*-
# @File  : majority_element.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :


class Solution1:
    """ 使用hash表
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def majorityElement(self, nums):
        value_counts = {}
        size = len(nums)
        for item in nums:
            if item not in value_counts:
                value_counts[item] = 1
            else:
                value_counts[item] += 1
            if value_counts[item] > size/2:
                return item


def main():
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.majorityElement(test_case))


if __name__ == '__main__':
    main()
