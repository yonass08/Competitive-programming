# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            Next = self.swapPairs(head.next.next)
            head.next.next = head
            prev = head.next
            head.next = Next
            return prev
        else:
            return head
