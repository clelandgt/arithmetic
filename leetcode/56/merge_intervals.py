# -*- coding: utf-8 -*-
# @File  : merge_intervals.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-17
# @Desc  :
from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        start, end = None, None
        first = True
        for interval in intervals:
            if first:
                start, end = interval[0], interval[1]
                first = False
                continue
            if end < interval[0]:
                result.append([start, end])
                start, end = interval[0], interval[1]
            elif end >= interval[0]:
                end = interval[1] if end < interval[1] else end
        if start and end:
            result.append([start, end])

        return result


def main():
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        []
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.merge(test_case))


if __name__ == '__main__':
    main()
