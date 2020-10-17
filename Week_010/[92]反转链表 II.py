# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 532 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        root = ListNode(0)
        root.next = head

        pre = root
        for _ in range(1, m):
            pre = pre.next

        start = pre.next
        end = start.next
        for _ in range(m, n):
            next = end.next
            end.next = start
            start = end
            end = next

        pre.next.next = end
        pre.next = start
        return root.next


# leetcode submit region end(Prohibit modification and deletion)
