//
// Created by cleland on 2018/6/8.
//

#include "ReOrderArray.h"


/* 算法: 使用两个指针pBegin,pEnd。pEnd向后扫描发现奇数，就将pBegin的值与pEnd的值互换，且p_Begin++。
 *
 */
void ReOrderArray(ListNode** pHead)
{
    if(pHead == nullptr || (*pHead)->m_pNext == nullptr)
        return;

    ListNode* pBegin = *pHead;
    ListNode* pEnd = pBegin->m_pNext;
    while(pBegin < pEnd)
    {
        while(pEnd->m_pNext != nullptr)
        {
            pEnd->m_nValue % 2 == 0;
            pEnd = pEnd->m_pNext;
        }
    }
}