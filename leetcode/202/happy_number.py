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
        except KeyError:
            self.repeat_dict[total] = 1
            return self.isHappy(total)


class Solution2:
    """
    执行时间 52ms
    时间复杂度超过：5.82%
    空间复杂度超过：100%
    """
    def __init__(self):
        self.repeat_dict = {}

    def isHappy(self, n: int) -> bool:
        total = sum([int(item) **2 for item in str(n)])
        if total == 1:
            return True

        try:
            self.repeat_dict[total]
            return False
        except KeyError:
            self.repeat_dict[total] = 1
            return self.isHappy(total)


class Solution3:
    """
    时间复杂度超过：5.82%
    空间复杂度超过：100%
    """
    def __init__(self):
        self.repeat = set()

    def isHappy(self, n: int) -> bool:
        total = sum([int(item) **2 for item in str(n)])
        if total == 1:
            return True
        if total not in self.repeat:
            self.repeat.add(total)
            return self.isHappy(total)
        else:
            return False


def main():
    s = Solution2()
    print(s.isHappy(19))


if __name__ == '__main__':
    main()
    # print(split_nums(199))
