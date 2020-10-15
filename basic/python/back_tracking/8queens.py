# -*- coding: utf-8 -*-
# @File  : 8queens.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-24
# @Desc  :

""" 问题描述
8*8的棋盘, 往里放8个棋子(皇后), 每个棋子所在的行、列、对角线都不能有另一个棋子，找到所有满足这种要求的棋子。
"""

result = [0] * 8
N = 0


def cal_8queens(row):
    global result

    if row == 8:
        print_8queens(result)
        return

    # 遍历每行的每一列
    for column in range(8):
        if is_ok(row, column):
            result[row] = column
            cal_8queens(row+1)


def is_ok(row, column):
    """ 判断当前落地的棋子是否符合规则
    行，列，左右对角线不能有其他棋子. 只看符合规则的，而不是先全量再按照规则筛选
    :param row:
    :param column:
    :return:
    """
    global result
    left_diagonal, right_diagonal = column, column

    for index in range(row)[::-1]:
        left_diagonal -= 1
        right_diagonal += 1

        # 不在同列
        if result[index] == column:
            return False
        # 不在左对角线
        if left_diagonal >= 0:
            if result[index] == left_diagonal:
                return False
        if right_diagonal < 8:
            if result[index] == right_diagonal:
                return False

    return True


def print_8queens(result):
    """打印8皇后"""
    global N
    N += 1
    print(f'解法 {N}')
    for i in range(8):
        for j in range(8):
            if result[i] == j:
                print('Q', end=' ')
            else:
                print('*', end=' ')
        print('\n')


def main():
    cal_8queens(0)


if __name__ == '__main__':
    main()
