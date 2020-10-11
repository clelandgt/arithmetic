# -*- coding: utf-8 -*-
# @File  : simple_browser.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-11
# @Desc  :

import sys
# 引用当前文件夹下的stack_by_linked
sys.path.append('stack_by_linked.py')
from stack_by_linked import Stack


class Browser():
    def __init__(self):
        self.__forward = Stack()
        self.__back = Stack()

    def can_back(self):
        if self.__forward.is_empty():
            return False
        return True

    def can_forward(self):
        if self.__back.is_empty():
            return False
        return True

    def open(self, url):
        print('new open url: ', url)
        self.__forward.push(url)

    def back(self):
        if not self.can_back():
            return

        value = self.__forward.pop()
        print('back url: ', self.__forward.top())
        self.__back.push(value)

    def forward(self):
        if not self.can_forward():
            return

        value = self.__back.pop()
        print('forward url: ', value)
        self.__forward.push(value)


def main():
    bs = Browser()
    print('-- open')
    bs.open('url1')
    bs.open('url2')
    bs.open('url3')
    bs.open('url4')
    bs.open('url5')

    print('-- back')
    bs.back()
    bs.back()
    print('-- forward')
    bs.forward()

    print('-- open')
    bs.open('url6')
    bs.open('url7')

    print('-- forward')
    bs.forward()

    print('-- back')
    bs.back()
    bs.back()

    print('-- forward')
    bs.forward()
    bs.forward()


if __name__ == '__main__':
    main()
