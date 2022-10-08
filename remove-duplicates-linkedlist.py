# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        while left:
            right = left.next
            while right and left.val == right.val:
                temp = right
                right = right.next
                left.next = right
                temp.next = None
                del(temp)
            left = left.next
        return head
