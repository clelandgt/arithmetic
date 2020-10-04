# -*- coding: utf-8 -*-
# @File  : merge_sort_array.py
# @Author: tao.gan@advance.ai
# @Date  : 2020-10-04
# @Desc  : https://blog.csdn.net/weixin_43633501/article/details/90110565


def merge_sort_array(nums1, nums2):
    results = []
    while len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] <= nums2[0]:
            results.append(nums1[0])
            del nums1[0]
        else:
            results.append(nums2[0])
            del nums2[0]
    results.extend(nums1)
    results.extend(nums2)
    return results


def print_array(nums):
    print(nums)


def main():
    num1 = [2, 6, 9, 12, 20]
    num2 = [1, 3, 11, 12, 18]
    print(merge_sort_array(num1, num2))


if __name__ == '__main__':
    main()
