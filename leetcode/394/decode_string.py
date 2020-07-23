# -*- coding: utf-8 -*-
# @File  : decode_string.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-23
# @Desc  :


class Solution1:
    def decodeString(self, s: str) -> str:
        num = 0
        string = ''
        stack_str = []
        stack_num = []

        for item in s:
            if item.isdigit():
                num = num * 10 + int(item)
            elif item == '[':
                stack_str.append(string)
                stack_num.append(num)
                string = ''
                num = 0
            elif item.isalpha():
                string += item
                num = 0
            elif item == ']':
                pre_string = stack_str.pop()
                pre_string += (string * stack_num.pop())
                string = pre_string
                num = 0

        return string


def main():
    test_cases = [
        '3[a]2[bc]',
        '3[a2[c]]',
        '2[abc]3[cd]ef',
        'abc13[cd]xyz'
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.decodeString(test_case))


if __name__ == '__main__':
    main()

