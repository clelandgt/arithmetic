# -*- coding: utf-8 -*-
# @File  : valid_parentheses.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-22
# @Desc  :


class Solution1:
    def isValid(self, s: str) -> bool:
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for item in s:
            if item in match:
                if not (stack and stack.pop() == match[item]):
                    return False
            else:
                stack.append(item)
        return not stack


def main():
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]

    print('Solution1')
    s1 = Solution1()
    for test_case in test_cases:
        print(s1.isValid(test_case))


if __name__ == '__main__':
    main()
