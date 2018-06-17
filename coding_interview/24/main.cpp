#include <iostream>
#include "reverse_list.h"


void Test1()
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
    printf("After reverse list:\n");
    ListNode* pResult = ReverseList(pNode1);
    PrintList(pResult);
    DestroyList(pNode1);

}

// 链表为空
void Test2()
{
    ListNode* pNode1 = nullptr;
    PrintList(pNode1);
    printf("After reverse list:\n");
    ListNode* pResult = ReverseList(pNode1);
    PrintList(pResult);
    DestroyList(pNode1);
}

// 链表只有一个节点
void Test3()
{
    ListNode* pNode1 = CreateListNode(1);
    PrintList(pNode1);
    printf("After reverse list:\n");
    ListNode* pResult = ReverseList(pNode1);
    PrintList(pResult);
    DestroyList(pNode1);
}

int main()
{
    Test1();
    return 0;
}