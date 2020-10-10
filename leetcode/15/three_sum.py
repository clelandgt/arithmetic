# -*- coding: utf-8 -*-
# @File  : three_sum.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-10
# @Desc  : https://leetcode-cn.com/problems/3sum/


class Solution1(object):
    def threeSum(self, nums):
        pass


def main():
    test_cases = [
        (-1, 0, 1, 2, -1, -4)
    ]

    s1 = Solution1()
    for test_case in test_cases:
        print(s1.threeSum(test_case))


if __name__ == '__main__':
    main()
