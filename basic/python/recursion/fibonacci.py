# -*- coding: utf-8 -*-
# @File  : fibonacci.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  : f(n) = f(n-1) + f(n-2)  0、1、1、2、3、5、8、13、21、34


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def main():
    for i in range(0, 11):
        print(fibonacci(i))


if __name__ == '__main__':
    main()
