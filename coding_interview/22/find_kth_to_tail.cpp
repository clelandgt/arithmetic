//
// Created by cleland on 2018/6/11.
//
#include "find_kth_to_tail.h"

ListNode* FindKthToTail1(ListNode* pListHead, unsigned int k)
{

    ListNode* pNode = pListHead;

    if(pNode == nullptr)
        return nullptr;

    // 得到链表的长度
    unsigned int unLength = 1;
    while (pNode->m_pNext!= nullptr)
    {
        pNode = pNode->m_pNext;
        unLength++;
    }

    // 遍历倒数第k个节点
    pNode = pListHead;
    if (k > unLength)
        return nullptr;
    for (int i=2; i <= unLength - k +1; i++)
    {
        pNode = pNode->m_pNext;
    }
    return pNode;
}


/* 算法：使用两个指针，第一个指针遍历到k个节点时，第二个节点开始从头结点开始遍历。当第一个指针遍历到尾节点时，返回第二个指针。
* 特殊情况：1. 链表为空； 2. 当第一个指针还未遍历到k节点时，就已经结束。
*/
ListNode* FindKthToTail2(ListNode* pListHead, unsigned int k)
{
    if (pListHead == nullptr || k ==0 )
        return nullptr;

    ListNode* pFirstPoint = pListHead;

    for(unsigned int unIndex = 1; unIndex < k; unIndex++)
    {
        if(pFirstPoint->m_pNext== nullptr)
            return nullptr;
        pFirstPoint = pFirstPoint->m_pNext;
    }

    ListNode* pSecondPoint = pListHead;
    while(pFirstPoint->m_pNext!= nullptr)
    {
        pFirstPoint = pFirstPoint->m_pNext;
        pSecondPoint = pSecondPoint->m_pNext;
    }

    return pSecondPoint;
}