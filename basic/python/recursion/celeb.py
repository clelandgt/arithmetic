# -*- coding: utf-8 -*-
# @File  : celeb.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-11
# @Desc  : [Python算法教程][第4章 归纳、递归与规归简][基于归纳法(与递归法)的设计][4.4.1寻找最大排列]
from random import randrange


def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v] and not G[v][u]:
                break
        else:
            return u
    return None


def main():
    # 创建随机图
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]

    # 构建一个明星
    c = randrange(n)
    print('randrange: ', format(c))
    for i in range(n):
        G[i][c] = True
        G[c][i] = False
    print('native_celleb: ', naive_celeb(G))


if __name__ == '__main__':
    main()