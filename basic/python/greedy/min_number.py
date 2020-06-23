# -*- coding: utf-8 -*-
# @File  : min_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-23
# @Desc  :

""" 问题描述
问题：在一个非负数整数a中，我们希望从中移除k个数字，让剩下的数字值最小，如何选择移除那k个数字
解题思路：由高位开始，比较低一位，如果高位大，则删除高位数据。否则比较后面的两个数字
"""


def get_min_number(number, k):
    if len(str(number)) < k:
        return 0

    nums = list(str(number))
    index = 0
    while k > 0:
        if nums[index] > nums[index+1]:
            del nums[index]
            index -= 1
            k -= 1
        else:
            index += 1

    return int(''.join(nums))


def main():
    number = 3455473145238
    k = 5
    print('length: ', len(str(number)))

    result = get_min_number(number, k)
    print('get_min_number1 result: ', result)
    print('length: ', len(str(result)))


if __name__ == '__main__':
    main()
