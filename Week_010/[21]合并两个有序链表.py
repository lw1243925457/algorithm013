# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1290 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        while l1 or l2:
            if not l1:
                ans.append(l2.val)
                l2 = l2.next
            elif not l2:
                ans.append(l1.val)
                l1 = l1.next
            elif l1 and l2:
                if l1.val < l2.val:
                    ans.append(l1.val)
                    l1 = l1.next
                else:
                    ans.append(l2.val)
                    l2 = l2.next

        # print(ans)
        if not ans:
            return None
        l = ListNode(ans[0])
        p = l
        for i in range(1, len(ans)):
            p.next = ListNode(ans[i])
            p = p.next
        return l


# leetcode submit region end(Prohibit modification and deletion)
