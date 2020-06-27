# -*- coding: utf-8 -*-
# @File  : top_k_frequent_elements.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-27
# @Desc  :
from typing import List


class Solution1:
    """
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for num in nums:
            if result.get(num):
                result[num] += 1
            else:
                result[num] = 1

        return [item[0] for item in sorted(result.items(), key=lambda item: item[1], reverse=True)][:k]


def main():
    test_cases = [
        {'nums': [1, 1, 1, 2, 2, 4], 'k': 2},
        {'nums': [1], 'k': 1},
    ]

    print('***** Solution1 *****')
    s = Solution1()
    for test_case in test_cases:
        print(s.topKFrequent(test_case['nums'], test_case['k']))




if __name__ == '__main__':
    main()
