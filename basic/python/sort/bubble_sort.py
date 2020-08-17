# -*- coding: utf-8 -*-
# @File  : bubble_sort.py
# @Author: clelandgt@163.com
# @Date  : 2020-03-02
# @Desc  : 冒泡


def bubble_sort(nums):
    """ 冒泡排序O(n^2)
    每次比较如果发现较小的元素在后面，就交换两个相邻的元素。排序序列顺序从左到右是从小到大，伪代码：
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums))[::-1]:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums


def main():
    nums1 = [5, 2, 4, 6, 10, 1, 3, 1, 23, 2, 9]
    print('before sort:', nums1)
    nums2 = bubble_sort(nums1)
    print('after sort:', nums2)


if __name__ == '__main__':
    main()
