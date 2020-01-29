# -*- coding: utf-8 -*-
# @File  : count_primes.py
# @Author: clelandgt@163.com
# @Date  : 2020-01-28
# @Desc  : https://leetcode.com/problems/count-primes/
# There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 质数: 指整数在一个大于1的自然数中,除了1和此整数自身外,没法被其他自然数整除的数。
# 当前一直超时，未解决。


class Solution1:
    """ 依次判断是否是素数。素数的判断方法：依次除以2~n.
    O(n^2)
    """
    def countPrimes(self, n: int) -> int:
        sum = 0
        if n <= 1:
            return sum

        for i in range(2, n):
            j = 2
            primes = True
            while j < i:
                if i % j == 0:
                    j = i
                    primes = False
                else:
                    j += 1
            if primes:
                sum += 1

        return sum


class Solution:
    """ 依次判断是否是素数。素数的判断方法：依次除以2~n开方.
    O(n^2)
    """
    def is_primes(self, n: int) -> int:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0
        return 1

    def countPrimes(self, n: int) -> int:
        sum = 0
        if n <= 1:
            return sum

        for i in range(2, n):
            sum += self.is_primes(i)

        return sum


def main():
    s = Solution()
    print(s.countPrimes(999983))


if __name__ == '__main__':
    main()
