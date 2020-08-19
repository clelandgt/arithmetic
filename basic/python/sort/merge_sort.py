# -*- coding: utf-8 -*-
# @File  : merge_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 归并排序


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(nums):
    """ 归并排序
    时间复杂度：O(nlogn)
    该算法是采用分治的一种非常典型的应用。
    1. 将已有序的子序列合并，并得到完全有序的序列；
    2. 先使命每个子序列有序，再使子序列段间有序。若将两个有序表合成一个有序表，称为二路合并。
    """
    size = len(nums)
    if size == 1:
        return nums
    mid = int(size / 2)
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def main():
    test_cases = [
        [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    ]

    for test_case in test_cases:
        print('before sort:', test_case)
        print('after sort:', merge_sort(test_case))


if __name__ == '__main__':
    main()
