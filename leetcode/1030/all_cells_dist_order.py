# -*- coding: utf-8 -*-
# @File  : all_cells_dist_order.py
# @Author: clelandgt@163.com
# @Date  : 11/17/20
# @Desc  :
from typing import List


class Solution1:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = {}

        for row in range(R):
            for column in range(C):
                result[(row, column)] = abs(row-r0) + abs(column-c0)
        items = sorted(result.items(), key=lambda x: x[1])
        return [item[0] for item in items]


def main():
    test_cases = [
        (1, 2, 0, 0),
        (2, 2, 0, 1),
        (2, 3, 1, 2),
    ]
    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.allCellsDistOrder(test_case[0], test_case[1], test_case[2], test_case[3]))


if __name__ == '__main__':
    main()
