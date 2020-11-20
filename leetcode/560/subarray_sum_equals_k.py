# -*- coding: utf-8 -*-
# @File  : subarray_sum_equals_k.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-25
# @Desc  :
from typing import List


class Solution1:
    """暴力破解 (超时)
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total, dict_grand = 0, {0: 1}
        for num in nums:
            total += num
            if total-k in dict_grand:
                res += dict_grand[total-k]
            dict_grand[total] = dict_grand.get(total, 0) + 1

        return res


def main():
    test_cases = [
        ([1, 1, 1], 2),
        ([0,0,0,0,0,0,0,0,0,0], 0)
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.subarraySum(test_case[0], test_case[1]))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.subarraySum(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
