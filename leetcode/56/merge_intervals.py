# -*- coding: utf-8 -*-
# @File  : merge_intervals.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-17
# @Desc  :
from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        start = None
        end = None
        for interval in intervals:
            if len(result) == 0:
                pass


def main():
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]]
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.merge(test_case))


if __name__ == '__main__':
    main()
