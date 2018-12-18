# -*- coding:utf-8 -*-
__author__ = 'cleland'


def insert_sort(l):
    """ 插入排序
    """
    for i in xrange(1, len(l)):
        for j in xrange(0, i):
            if l[i] <= l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print 'before sort:', l1
    l2 = insert_sort(l1)
    print 'after sort:', l2


if __name__ == '__main__':
    main()
