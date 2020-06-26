# -*- coding: utf-8 -*-
# @File  : single_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-21
# @Desc  : https://leetcode.com/problems/single-number/
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        """
        时间复杂度： O(n)
        空间复杂度： O(n)
        :param nums:
        :return:
        """
        result = []
        for item in nums:
            if item not in result:
                result.append(item)
            else:
                result.remove(item)
        return result.pop()


class Solution2:
    """ 使用散列表
        时间复杂度： O(n)
        空间复杂度： O(n)
    """
    def singleNumber(self, nums: List[int]) -> int:
        tmp_dict = {}
        for item in nums:
            if item not in tmp_dict.keys():
                tmp_dict[item] = 1
            else:
                tmp_dict.pop(item)
        return tmp_dict.popitem()[0]


class Solution3:
    """ 使用散列表+异常处理
        时间复杂度： O(n)
        空间复杂度： O(n)
    """
    def singleNumber(self, nums: List[int]) -> int:
        tmp_dict = {}
        for item in nums:
            try:
                tmp_dict.pop(item)
            except:
                tmp_dict[item] = 1
        return tmp_dict.popitem()[0]


class Solution4:
    """ math
        2∗(a+b+c)−(a+a+b+b+c)=c

        时间复杂度: O(1)
        空间复杂度: O(1)
    :return:
    """
    def singleNumber(self, nums: List[int]) -> int:
        nums_distinct = set(nums)
        return sum(nums_distinct) * 2 - sum(nums)


def main():
    # Input: [4,1,2,1,2], Output: 4
    nums = [4, 1, 2, 1, 2]
    s = Solution4()
    print(s.singleNumber(nums))


if __name__ == '__main__':
    main()
