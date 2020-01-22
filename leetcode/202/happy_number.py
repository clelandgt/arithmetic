# -*- coding: utf-8 -*-
# @File  : happy_number.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-22
# @Desc  : https://leetcode.com/problems/happy-number/


def split_nums(num):
    """ 整数分隔成一个个数字，但这里是逆序 """
    if num == 0:
        return 0
    if num < 0:
        return False

    result = []
    while num > 0:
        result.append(num % 10)
        num = int(num/10)
    return result


class Solution1:
    def __init__(self):
        self.repeat_dict = {}

    def split_nums(self, num):
        """ 整数分隔成一个个数字，但这里是逆序 """
        if num == 0:
            return 0
        if num < 0:
            return False

        result = []
        while num > 0:
            result.append(num % 10)
            num = int(num / 10)
        return result

    def isHappy(self, n: int) -> bool:
        total = 0
        items = self.split_nums(n)
        for item in items:
            total += item ** 2
        if total == 1:
            return True

        try:
            self.repeat_dict[total]
            return False
        except Exception:
            self.repeat_dict[total] = 1
            return self.isHappy(total)


def main():
    s = Solution1()
    print(s.isHappy(19))


if __name__ == '__main__':
    main()
    # print(split_nums(199))
