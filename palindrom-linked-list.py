# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        fast = slow

        while slow:
            fast = slow.next
            slow.next = prev
            prev = slow
            slow = fast

        forward = head
        backward = prev

        while backward:
            if forward.val != backward.val: return False
            backward = backward.next
            forward = forward.next

        return True
        
