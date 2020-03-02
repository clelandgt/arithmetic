# -*- coding: utf-8 -*-
# @File  : insert_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 插入排序
"""
已排序的[0, n-1]加入n后再排序。
"""


def insert_sort(l):
    """基于循环"""
    for i in range(len(l)):
        for j in range(1, i+1)[::-1]:
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    return l


def insert_sort2(l):
    """基于递归"""
    return _insert_sort2(l, len(l))


def _insert_sort2(l, n):
    if n == 0:
        return
    _insert_sort2(l, n-1)

    for i in range(1, n)[::-1]:
        if l[i] < l[i-1]:
            l[i], l[i-1] = l[i-1], l[i]

    return l


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print('before sort:', l1)
    l2 = insert_sort2(l1)
    print('after sort:', l2)


if __name__ == '__main__':
    main()