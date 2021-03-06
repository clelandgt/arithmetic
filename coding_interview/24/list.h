//
// Created by cleland on 2018/6/17.
//

#ifndef INC_24_LIST_H
#define INC_24_LIST_H

#endif //INC_24_LIST_H

struct ListNode
{
    int       m_nValue;
    ListNode* m_pNext;
};


ListNode* CreateListNode(int value);
void ConnectListNodes(ListNode* pCurrent, ListNode* pNext);
void PrintListNode(ListNode* pNode);
void PrintList(ListNode* pHead);
void DestroyList(ListNode* pHead);
void AddToTail(ListNode** pHead, int value);
void RemoveNode(ListNode** pHead, int value);
