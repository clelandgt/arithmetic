# -*- coding:utf-8 -*-
__author__ = 'cleland'


def selection_sort(l):
    """ 选择排序
    冒泡算法，每次比较如果发现较小的元素在后面，就交换两个相邻的元素。而选择排序算法的改进在于得到所谓的最小值时再做交换
    序列顺序从左到右是从小到大，伪代码：
    for i in [0, n):
        min_index = i
        for j in (i, n-1]:
            if l[j] < l[min_index]:
                min_index = j
        swap(l[i], l[min_index])
    """
    for i in range(0, len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

    return l


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print ('before sort:', l1)
    l2 = selection_sort(l1)
    print ('after sort:', l2)


if __name__ == '__main__':
    main()

