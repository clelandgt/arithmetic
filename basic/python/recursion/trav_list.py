# -*- coding: utf-8 -*-
# @File  : trav_list.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-08
# @Desc  : 使用递归遍历列表


def trav_list(nums, result=[], i=0):
    if i == len(nums):
        return
    trav_list(nums, result, i+1)
    result.append(nums[i])
    return result


def main():
    nums = range(100, 200)
    print(trav_list(nums))


if __name__ == '__main__':
    main()