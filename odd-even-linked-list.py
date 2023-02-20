# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        even_start = ListNode(0, None)
        even = even_start

        curr = head

        while curr.next:
            even.next = curr.next
            even = even.next
            curr.next = curr.next.next
            if curr.next:
                curr = curr.next
            else:
                break

        even.next = None
        curr.next = even_start.next
        return head
