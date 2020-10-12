# -*- coding: utf-8 -*-
# @File  : mySqrt.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-12
# @Desc  :


class Solution1:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        result = int(x / 2)
        while True:
            if result ** 2 == x:
                return result
            elif result ** 2 > x:
                result = int(result / 2)
            else:
                break

        for i in range(result, result * 2 + 2):
            if i ** 2 > x:
                return i - 1
            elif i ** 2 == x:
                return i


def main():
    test_cases = [
        0,
        1,
        2,
        6,
        4,
        8,
        9,
        625
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.mySqrt(test_case))


if __name__ == '__main__':
    main()
