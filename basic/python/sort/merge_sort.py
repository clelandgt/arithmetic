# -*- coding:utf-8 -*-
""" 归并排序
"""

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(l):
    """ 归并算法
    该算法是采用分治的一种非常典型的应用。
    1. 将已有序的子序列合并，并得到完全有序的序列；
    2. 先使命每个子序列有序，再使子序列段间有序。若将两个有序表合成一个有序表，称为二路合并。
    """
    if len(l) <= 1:
        return l
    middle = len(l) / 2
    left = merge_sort(l[:middle])
    right =merge_sort(l[middle:])
    return merge(left, right)


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print 'before sort:', l1
    l2 = merge_sort(l1)
    print 'after sort:', l2


if __name__ == '__main__':
    main()
