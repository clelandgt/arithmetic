//
// Created by cleland on 2018/6/26.
//

#ifndef BINARY_TREE_BINARY_TREE_H
#define BINARY_TREE_BINARY_TREE_H

struct SBinaryTreeNode{
    int nValue;
    SBinaryTreeNode* pLift;
    SBinaryTreeNode* pRight;
    SBinaryTreeNode(int nValue): nValue(nValue), pLift(nullptr), pRight(nullptr){};
};

class CBinaryTree{
private:
    SBinaryTreeNode* m_pRoot;
private:
    void Destroy(SBinaryTreeNode* m_pRoot);

public:
    CBinaryTree();
    ~CBinaryTree();
    bool Insert(int nValue);
    bool Delete(int nValue);
    SBinaryTreeNode* Find(int nValue) const;

    // 遍历：前序，中序，后序。
    void PreOrder(SBinaryTreeNode* pRoot);
    void InOrder(SBinaryTreeNode* pRoot);
    void PostOrder(SBinaryTreeNode* pRoot);
};


#endif //BINARY_TREE_BINARY_TREE_H
