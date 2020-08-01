# -*- coding: utf-8 -*-
# @File  : climbing_stairs.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-01
# @Desc  :


class Solution1:
    """使用传统递归超时"""
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution2:
    """循环解决"""
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n

        a, b = 1, 1
        for _ in range(2, n+1):
            tmp = a
            a = a + b
            b = tmp
        return a


def main():
    test_cases = [2, 3]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.climbStairs(test_case))

    print('Solution2')
    s2 = Solution2()
    for test_case in test_cases:
        print(s2.climbStairs(test_case))


if __name__ == '__main__':
    main()
