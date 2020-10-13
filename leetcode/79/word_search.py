# -*- coding: utf-8 -*-
# @File  : word_search.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-13
# @Desc  : https://leetcode-cn.com/problems/word-search/
from typing import List


class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    pass
    def _search(self, board, word):


def main():
    test_cases = [
        ([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'ABCCED'),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], 'SEE'),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], 'ABCB')
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        s1.exist(test_case)



if __name__ == '__main__':
    main()
