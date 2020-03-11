# -*- coding: utf-8 -*-
# @File  : get_min_distance_pointers.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-11
# @Desc  :

"""
问题描述:
    二维平面上有 n 个点，如何快速计算出两个距离最近的点对
法一: 暴力求解O(n^2)
"""


def get_min_distance_pointers1(pointers):
    pointer1 = None
    pointer2 = None
    min_distance = float('inf')
    """ 暴力求解 """
    for i in range(len(pointers)):
        for j in range(i+1, len(pointers)):
            distance = ((pointers[i][0]-pointers[j][0]) ** 2 + (pointers[i][1]-pointers[j][1]) ** 2) ** 0.5
            if distance <= min_distance:
                min_distance = distance
                pointer1 = pointers[i]
                pointer2 = pointers[j]
    return pointer1, pointer2


def main():
    pointers = [[1, 1], [9, 3], [4, 5], [-1, -2]]
    print('min distance: ', get_min_distance_pointers1(pointers))


if __name__ == '__main__':
    main()