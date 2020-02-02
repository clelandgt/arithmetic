# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: clelandgt@163.com
# @Date  : 2020-02-01
# @Desc  :
from . import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super(__class__, self).__init__()


def main():
    tree = BinarySearchTree()
    tree.insert(13)
    tree.insert(10)
    tree.insert(16)
    tree.insert(9)
    tree.insert(11)
    tree.insert(14)
    tree.insert(17)
    tree.insert(8)


    """
                  13
                /  / \
              10   14 16
              / \      \   
             9  11     17
            /    
           8     
    """

    min_value = tree.get_min()
    print ('trees min value: {}'.format(min_value))

    max_value = tree.get_max()
    print ('trees max value: {}'.format(max_value))

    result = tree.find(10)
    print ('find 10 in tree, result: {}'.format(result.value))

    print (u'前序遍历:')
    tree.pre_order(tree.root)

    print (u'中序遍历:')
    tree.in_order(tree.root)

    print (u'后序遍历:')
    tree.bac_order(tree.root)


if __name__ == '__main__':
    main()