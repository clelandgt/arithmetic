# -*- coding:utf-8 -*-
__author__ = 'cleland'


def insert_sort1(nums):
    """插入排序 循环的方式实现"""
    for i in range(1, len(nums)):
        for j in range(1, i+1)[::-1]:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]

    return nums


def insert_sort2(nums):
    """插入排序 递归的方式实现"""
    return _insert_sort2(nums, len(nums))


def _insert_sort2(nums, n):
    if n == 0:
        return
    # 对于n-1进行排序
    _insert_sort2(nums, n-1)
    # 将n加入已排序的n-1序列里

    for i in range(1, n)[::-1]:
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            break

    return nums


def main():
    l1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print ('before sort:', l1)
    l2 = insert_sort2(l1)
    print ('after sort:', l2)


if __name__ == '__main__':
    main()
