"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
通过次数322,219提交次数507,432


解题思路：
1 刷
用一个数组保存值，比较列表，小的值放入
还原成链表返回即可
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        while l1 is not None or l2 is not None:
            if l1 is None:
                l.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                l.append(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                l.append(l1.val)
                l1 = l1.next
            else:
                l.append(l2.val)
                l2 = l2.next
        if len(l) == 0:
            return None
        l3 = ListNode(l[0])
        head = l3
        for i in range(1, len(l)):
            l3.next = ListNode(l[i])
            l3 = l3.next
        return head


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    head = s.mergeTwoLists(l1, l2)
    while head is not None:
        print(head.val)
        head = head.next
