//
// Created by cleland on 2018/6/11.
//

#ifndef INC_22_FIND_KTH_TO_TAIL_H
#define INC_22_FIND_KTH_TO_TAIL_H

#endif //INC_22_FIND_KTH_TO_TAIL_H

#include "list.h"
/* 问题描述：输入一个链表，输出该链表中倒数第k个结点。
 * */


// 算法: 遍历两次：第一次获取链表的长度，第二次遍历到length-k+1,该节点就是倒数第k个节点；
ListNode* FindKthToTail1(ListNode* pListHead, unsigned int k);


/* 算法：使用两个指针，第一个指针遍历到k个节点时，第二个节点开始从头结点开始遍历。当第一个指针遍历到尾节点时，返回第二个指针。
* 特殊情况：1. 链表为空； 2. 当第一个指针还未遍历到k节点时，就已经结束。
*/
ListNode* FindKthToTail2(ListNode* pListHead, unsigned int k);