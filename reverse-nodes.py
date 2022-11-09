# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        if not head: return None

        count = 1
        curr = head
        while curr.next and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head

        prev = self.reverseKGroup(curr.next, k)
        curr.next = None
        curr = head

        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next

        return prev
