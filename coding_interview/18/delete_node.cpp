/** 在O(1)时间内删除链表节点
 * 问题：给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
 * 解决：删除i节点：将j节点的内容复制到i节点，然后将i节点的next指向j的next，最后删除j节点，就完成了删除i节点。
 * 边界：1. 只有单个节点(直接置节点为null)； 2. 删除的是尾节点(只能顺序遍历)
*/
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

struct ListNode
{
    int       m_nValue;
    ListNode* m_pNext;
};

ListNode* CreateListNode(int value)
{
    ListNode* pNode = new ListNode();
    pNode->m_nValue = value;
    pNode->m_pNext = nullptr;

    return pNode;
}

void ConnectListNodes(ListNode* pCurrent, ListNode* pNext)
{
    if(pCurrent == nullptr)
    {
        printf("Error to connect two nodes.\n");
        exit(1);
    }

    pCurrent->m_pNext = pNext;
}

void DestroyList(ListNode* pHead)
{
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        pHead = pHead->m_pNext;
        delete pNode;
        pNode = pHead;
    }
}


void DeleteNode(ListNode** pListHead, ListNode* pToBeDeleted)
{
    if(!pListHead || !pToBeDeleted)
        return;

    if(pToBeDeleted->m_pNext != nullptr)
    {
        // 1. 多个节点删除的节点不是尾节点
        ListNode* pNextNode = pToBeDeleted->m_pNext;
        pToBeDeleted->m_nValue = pNextNode->m_nValue;
        pToBeDeleted->m_pNext = pNextNode->m_pNext;
        
        delete pNextNode;
        pNextNode = nullptr;
    }
    else if(*pListHead == pToBeDeleted)
    {
        // 2. 只有单个节点
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
        pListHead = nullptr;
    }
    else
    {
        // 3. 多个节点删除的节点是尾节点
        ListNode* pNode = *pListHead;
        while(pNode->m_pNext!=pToBeDeleted)
        {   
            pNode = pNode->m_pNext;
        }
        pNode->m_pNext = nullptr;
        delete pToBeDeleted;
        pToBeDeleted = nullptr;
    }
}


int main(int argc, char* argv[])
{   
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);

    ListNode* pHeader = pNode1;
    DeleteNode(&pHeader, pNode3);

    return 0;
}

