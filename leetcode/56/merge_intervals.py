# -*- coding: utf-8 -*-
# @File  : merge_intervals.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-17
# @Desc  :
from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1][1] = interval[1] if result[-1][1] < interval[1] else result[-1][1]
            else:
                result.append(interval)

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
