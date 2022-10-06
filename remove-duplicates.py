# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while True:
            if head == None or head.next == None:
                return head
            after = head.next
            if head.val == after.val:
                while after.next != None and head.val == after.val:
                    after = after.next
                if head.val == after.val:
                    return None
                head = after
            else:
                break
        
        start = head
        end = head.next
        
        while True:
            if end.next == None:
                return head
            elif end.val == end.next.val:
                while end.next != None and start.next.val == end.val:
                    end = end.next
                if start.next.val == end.val:
                    start.next = None
                    return head
                start.next = end
            else:
                start = end
                end = end.next
                    
                
        
