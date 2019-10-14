# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: gantao@huizhaofang.com
# @Date  : 2019-10-12
# @Desc  : 使用邻接表实现图


class Digraph(object):
    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, s, t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_tbl[s].append(t)
        return True

    def __len__(self):
        return self.v_num

    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError('No Such Vertex!')
        return self.adj_tbl[ind]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


class Undigraph(object):
    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, s, t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_tbl[s].append(t)
        self.adj_tbl[t].append(s)
        return True

    def __len__(self):
        return self.v_num

    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError('No Such Vertex!')
        return self.adj_tbl[ind]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


if __name__ == '__main__':
    dg = Digraph(10)
    dg.add_edge(1, 9)
    dg.add_edge(1, 3)
    dg.add_edge(3, 2)
    print('Digraph: ', dg.adj_tbl)

    ug = Undigraph(10)
    ug.add_edge(1, 9)
    ug.add_edge(1, 3)
    ug.add_edge(3, 2)
    print('Undigraph: ', ug.adj_tbl)