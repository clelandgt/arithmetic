# -*- coding: utf-8 -*-
# @File  : calc_sort_degree.py
# @Author: clelandgt@163.com
# @Date  : 2019-10-30
# @Desc  : https://time.geekbang.org/column/article/73503
"""
问题：假设我们有 n 个数据，我们期望数据从小到大排列，那完全有序的数据的有序度就是 n(n-1)/2，逆序度等于 0；
     相反，倒序排列的数据的有序度就是 0，逆序度是 n(n-1)/2。除了这两种极端情况外，我们通过计算有序对或者
     逆序对的个数，来表示数据的有序度或逆序度。
eg:  2,4,3,1,5,6 逆序个数为4：(2,1) (4,3) (4,1) (3,1)
"""
global result


def calc_sort_degree1(nums):
    """ 暴力求解直接遍历 O(n^2) """
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                result += 1
    return result


def calc_sort_degree2(nums):
    """ 分治实现
    左半截逆序度 + 右半截逆序度 + 左在右半截的逆序度(计算这个，就可以假设左右半截分别是有序。这样就和归并排序合并的环节相似)
    :param nums:
    :return:
    """
    global result
    print(_merge_sort(nums))
    return result


def _merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2
    left = _merge_sort(nums[:middle])
    right = _merge_sort(nums[middle:])
    return _merge(left, right)


def _merge(left, right):
    """ 两个子字符串合并 """
    sort_nums = []
    global result
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sort_nums.append(left[0])
            del left[0]
        else:
            result += len(left)
            sort_nums.append(right[0])
            del right[0]

    sort_nums.extend(left)
    sort_nums.extend(right)

    return sort_nums


def main():
    global result
    nums = [2, 4, 3, 1, 5, 6]
    result = 0
    print("sort degree: ", calc_sort_degree2(nums))


if __name__ == '__main__':
    main()
