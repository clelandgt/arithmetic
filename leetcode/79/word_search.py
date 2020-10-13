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
                    if self._search(board, word[1:], [[row, col]]):
                        return True
        return False

    def _search(self, board, word, indexs):
        if len(word) == 0:
            return True
        width, high = len(board[0]), len(board)
        current_char = word[0]
        pre_index = indexs[-1]
        if pre_index[1]-1 >= 0:
            if board[pre_index[0]][pre_index[1]-1] == current_char and [pre_index[0], pre_index[1]-1] not in indexs:
                if self._search(board, word[1:], indexs+[[pre_index[0], pre_index[1]-1]]):
                    return True
        if pre_index[1]+1 < width:
            if board[pre_index[0]][pre_index[1]+1] == current_char and [pre_index[0], pre_index[1]+1] not in indexs:
                if self._search(board, word[1:], indexs+[[pre_index[0], pre_index[1]+1]]):
                    return True
        if pre_index[0]-1 >= 0:
            if board[pre_index[0]-1][pre_index[1]] == current_char and [pre_index[0]-1, pre_index[1]] not in indexs:
                if self._search(board, word[1:], indexs+[[pre_index[0]-1, pre_index[1]]]):
                    return True
        if pre_index[0]+1 < high:
            if board[pre_index[0]+1][pre_index[1]] == current_char and [pre_index[0]+1, pre_index[1]] not in indexs:
                if self._search(board, word[1:], indexs+[[pre_index[0]+1, pre_index[1]]]):
                    return True
        return False

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
        print(s1.exist(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
