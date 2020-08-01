# -*- coding: utf-8 -*-
# @File  : search_a_2d_matix.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :


class Solution1:
    def searchMatrix(self, matrix, target):
        """突破点: 以此数构成的右底的正方形区域内，该数最大。"""
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        r, c = len(matrix)-1, 0
        while r >= 0 and c <= len(matrix[0]) - 1:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                c = c + 1
            else:
                r = r - 1
        return False


def main():
    test_case = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

    print('Solution1')
    s1 = Solution1()
    print(s1.searchMatrix(test_case, 5))
    print(s1.searchMatrix(test_case, 20))


if __name__ == '__main__':
    main()
