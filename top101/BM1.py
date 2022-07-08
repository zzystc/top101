from cgitb import reset
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        pre = None
        phead = head
        while phead:
            temp = phead.next
            phead.next = pre
            pre = phead
            phead = temp
        return pre

if __name__ == "__main__":
    l1 = create_linked_list(list({1,2,3}))
    solution = Solution()
    sorted_lists = solution.ReverseList(l1)
    resu = print_linked_list(sorted_lists)
    # print(resu)
    # print('{}',end = '')
    print(1,end = '')
    print(' ',end = '')
    print(1)
#输出：