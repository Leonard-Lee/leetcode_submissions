# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        tmp = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(tmp)

        return self.merge(left, right)

    def getMid(self, head: ListNode) -> ListNode:
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next

            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next
        
        