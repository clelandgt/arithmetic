#include <iostream>
#include "find_kth_to_tail.h"


void Test()
{
    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    PrintList(pNode1);
    ListNode* pResult = FindKthToTail2(pNode1, 4);
    printf("find_kth_to_tail function result: %d\n", pResult->m_nValue);
    DestroyList(pNode1);
}

int main()
{
    Test();
}