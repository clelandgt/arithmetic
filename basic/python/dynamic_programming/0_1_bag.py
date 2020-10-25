# -*- coding: utf-8 -*-
# @File  : 0_1_bag.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-24
# @Desc  : 使用动态规划解决 0-1背包问题


def knapsack(weight, n, w):
    """
    
    :param weight: 物品重量 
    :param n: 物品个数
    :param w: 背包可承载重量
    :return: 
    """
    states = [[False] * (w+1)] * n

    # 第一行
    states[0][0] = True
    if weight[0] <= w:
        states[0][weight[0]] = True

    # 其他行
    for i in range(1, n):
        # 1. 第i个物品不放入背包
        for j in range(w+1):
            if states[i-1][j] == True:
                states[i][j] = states[i-1][j]

        # 2. 第i个物品放入背包
        for j in range(w-weight[0]):
            if states[i-1][j] == True:
                states[i][j+weight[i]] == True

    # 输出结果
    for i in range(w+1)[::-1]:
        if states[n-1][i] == True:
            return i
    return 0


def main():
    test_cases = [
        ([2, 2, 4, 6, 3], 9)
    ]
    for test_case in test_cases:
        print(knapsack(test_case[0], len(test_case[0]), test_case[1]))


if __name__ == '__main__':
    main()
