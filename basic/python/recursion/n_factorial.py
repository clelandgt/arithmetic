# -*- coding: utf-8 -*-
# @File  : n_factorial.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :


def n_factorial(n):
    if n == 1:
        return 1
    return n * n_factorial(n-1)


def main():
    test_cases = [3, 4, 5]
    for test_case in test_cases:
        print(n_factorial(test_case))


if __name__ == '__main__':
    main()
