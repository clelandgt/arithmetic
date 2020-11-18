# -*- coding: utf-8 -*-
# @File  : all_cells_dist_order.py
# @Author: clelandgt@163.com
# @Date  : 11/17/20
# @Desc  :
import collections
from typing import List


class Solution1:
    """
    时间复杂度: 存储时O(n^2), 排序时O(nlogn)
    空间复杂度: O(n^2)
    """
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = {}

        for row in range(R):
            for column in range(C):
                result[(row, column)] = abs(row-r0) + abs(column-c0)
        items = sorted(result.items(), key=lambda x: x[1])
        return [item[0] for item in items]


class Solution2:
    """
    基于Solution1优化
    """
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [(i, j) for i in range(R) for j in range(C)]
        return sorted(result, key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))


class Solution3:
    """ 使用桶排序
    时间复杂度: 存储时O(n^2), 排序使用桶排序时O(n)
    空间复杂度: O(n^2)
    """
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        result = collections.defaultdict(list)
        max_dist = max(r0, R-r0-1) + max(c0, C-c0-1)

        for row in range(R):
            for column in range(C):
                result[abs(row-r0) + abs(column-c0)].append((row, column))
        ret = []
        for i in range(max_dist+1):
            ret.extend(result[i])
        return ret


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

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.allCellsDistOrder(test_case[0], test_case[1], test_case[2], test_case[3]))

    print('Solution3')
    s3 = Solution3()
    for test_case in test_cases:
        print(s3.allCellsDistOrder(test_case[0], test_case[1], test_case[2], test_case[3]))


if __name__ == '__main__':
    main()
