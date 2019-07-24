# -*- coding:utf-8 -*-

__author__ = 'cleland'


def bubble_sort(l):
    """ 冒泡排序
    每次比较如果发现较小的元素在后面，就交换两个相邻的元素。排序序列顺序从左到右是从小到大，伪代码：
    for i in [0, n)
        for j in [n-1, i) #逆序 
            if a[j] < a[j-1]
                swap(a[j], a[j-1])
    """
    for i in range(0, len(l)):
        for j in range(i+1, len(l))[::-1]:
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    return l


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print ('before sort:', l1)
    l2 = bubble_sort(l1)
    print ('after sort:', l2)


if __name__ == '__main__':
    main()
