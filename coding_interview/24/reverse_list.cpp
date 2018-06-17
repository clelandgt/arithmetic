//
// Created by cleland on 2018/6/15.
//
#include "reverse_list.h"



/* 使用3个指针(pPre, pNode, pNext)。
 * 执行流程：
 * 1. pNext = pNode->next;
 * 2. nNode->next = pPre;
 * 3. pPre=pNode; pNode=pNext;
 *
 * */
ListNode* ReverseList(ListNode* pHead)
{
    if(pHead == nullptr || pHead->m_pNext== nullptr)
        return pHead;

    ListNode* pReverseHeader = nullptr;
    ListNode* pNode = pHead;
    ListNode* pPrevNode = nullptr;

    while(pNode != nullptr)
    {
        ListNode* pNext = pNode->m_pNext;
        pNode->m_pNext = pPrevNode;
        if(pNext == nullptr)
            pReverseHeader = pNode;
        pPrevNode = pNode;
        pNode = pNext;
    }

    return pReverseHeader;
}