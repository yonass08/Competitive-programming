# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = head
        while end.next != None:
            end = end.next
            head = head.next
            if end.next != None:
                end = end.next
                
        return head
        
