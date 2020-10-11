# -*- coding: utf-8 -*-
# @File  : eval_rpn.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :
from typing import List


class Solution1(object):
    def evalRPN(self, tokens: List[str]) -> int:
        stack, operator = [], ['+', '-', '*', '/']
        for item in tokens:
            if item not in operator:
                stack.append(int(item))
            else:
                result = 0
                second_value = stack.pop()
                first_value = stack.pop()
                if item == '+':
                    result = first_value + second_value
                elif item == '-':
                    result = first_value - second_value
                elif item == '*':
                    result = int(first_value * second_value)
                elif item == '/':
                    result = int(first_value / second_value)
                else:
                    raise Exception('operator must be: +, -, *, /')
                stack.append(result)
        return stack.pop()


def main():
    test_cases = [
        ['2', '1', '+', '3', '*'],
        ['4', '13', '5', '/', '+'],
        ['10', '6', '9', '3', '+', '-11', '*', '/', '17', '+', '5', '+']
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.evalRPN(test_case))


if __name__ == '__main__':
    main()
