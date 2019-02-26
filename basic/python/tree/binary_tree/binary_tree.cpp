//
// Created by cleland on 2018/6/26.
//

#include "binary_tree.h"

CBinaryTree::CBinaryTree() {
    m_pRoot = nullptr;
}

CBinaryTree::~CBinaryTree() {
    if(m_pRoot != nullptr)
    {
        Destroy(m_pRoot);
        m_pRoot = nullptr;
    }

}

void CBinaryTree::Destroy(SBinaryTreeNode *m_pRoot) {
    if(m_pRoot!= nullptr)
    {
        Destroy(m_pRoot->pLift);
        Destroy(m_pRoot->pRight);
        delete m_pRoot;
    }
}

/* 根节点为空时，插入根节点，否则：
 * 如果插入数据比根节点小，继续遍历根节点的左边，否则遍历根节点的右边，直达遍历到叶节点进行插入。
 * */
bool CBinaryTree::Insert(int nValue) {
    if(m_pRoot == nullptr)
    {
        m_pRoot = new SBinaryTreeNode(nValue);
        return true;
    }
}

