//
// Created by cleland on 2018/6/7.
//
#include "delete_repeat_node.h"


/*算法：一直遍历知道当前节点<下n个节点；将n节点的地址赋值给当前节点。按照这种方式，知道遍历到尾指针。
 * 重复位置可能是链表的头/中/尾
 * */
void DeleteRepeatNode(ListNode** pHead)
{
    if(pHead == nullptr || *pHead == nullptr)
        return;

    ListNode* pNode = *pHead;
    while(pNode != nullptr)
    {
        ListNode *pNext = pNode->m_pNext;

        if(pNext != nullptr && pNode->m_nValue!=pNext->m_nValue)
        {
            pNode = pNode->m_pNext;
        }
        else
        {
            ListNode* pToBeDel = pNode->m_pNext;
            while(pToBeDel != nullptr && pNode->m_nValue == pToBeDel->m_nValue)
            {
                pNext = pToBeDel->m_pNext;
                delete pToBeDel;
                pToBeDel = nullptr;
                pToBeDel = pNext;
            }
            pNode->m_pNext = pNext;
            pNode = pNode->m_pNext;
        }

    }
}
