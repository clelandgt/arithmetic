# -*- coding: utf-8 -*-
# @File  : pattern.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-18
# @Desc  : 正则表达式


match = False


def match(text, pattern):
    global match
    match = False
    rmatch(text, pattern, 0, 0)
    return match


def rmatch(text, pattern, ti, pj):
    global match
    t_len, p_len = len(text), len(pattern)
    if pj == p_len:
        if ti == t_len:
            match = True
        return

    if pattern[pj] == '*':
        for item in range(ti, t_len):
            rmatch(text, pattern, item, pj+1)
    elif pattern[pj] == '?':
        rmatch(text, pattern, ti, pj+1)
        rmatch(text, pattern, ti+1, pj+1)
    elif pattern[pj] == text[ti] and ti <t_len:
        rmatch(text, pattern, ti+1, pj+1)


def main():
    test_cases = [
        ['123abc4', '*bc4'],
        ['123abc4', '1*4']
    ]

    for test_case in test_cases:
        print(match(test_case[0], test_case[1]))


if __name__ == '__main__':
    main()
