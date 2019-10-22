# -*- coding: utf-8 -*-
# @File  : bm.py
# @Author: clelandgt@163.com
# @Date  : 2019-10-17
# @Desc  :
from typing import List

SIZE = 128


def _generate_bad_character_table(pattern: str) -> List[int]:
    table = [-1] * SIZE
    for index, item in enumerate(pattern):
        table[ord(item)] = index
    return table


def bad_character_rule(s: str, pattern: str) -> int:
    bad_character_table = _generate_bad_character_table(pattern)
    n, m = len(s), len(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            if s[i+j] != pattern[j]:
                si = i+j
                xi = bad_character_table[ord(s[i+j])]
                i += si - xi
                break
            else:
                j -= 1
        if j < 0: return i

    return -1


def main():
    s = 'hello world tao'
    pattern = 'wo'
    print('Bad Character Search Result: ', bad_character_rule(s, pattern))


if __name__ == '__main__':
    main()
