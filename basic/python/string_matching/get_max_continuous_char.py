# -*- coding: utf-8 -*-
# @File  : get_max_continuous_char.py
# @Author: clelandgt@163.com
# @Date  : 2020-09-26
# @Desc  : 字符串里连续出现次数最多的字符


def get_max_continuous_char(str1):
    if len(str1) == 0:
        return

    max_num = 0
    max_char = str1[0]
    i = 0
    while i < len(str1):
        for j in range(i, len(str1)):
            if str1[i] != str1[j]:
                break
        if j - i > max_num:
            max_num = j - 1
            max_char = str1[i]
        i = j + 1

    return max_char


def main():
    test_cases = [
        'adaffcccchhhe'
    ]

    for test_case in test_cases:
        print(get_max_continuous_char(test_case))


if __name__ == '__main__':
    main()
