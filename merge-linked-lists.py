# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pointer = result
        while list1 or list2:
            newNode = ListNode(None, None)
            pointer.next = newNode
            if list1 == None:
                newNode.val = list2.val
                pointer = newNode
                list2 = list2.next
            elif list2 == None:
                newNode.val = list1.val
                pointer = newNode
                list1 = list1.next
                
            elif list1.val < list2.val:
                newNode.val = list1.val
                pointer = newNode
                list1 = list1.next
                
            else:
                newNode.val = list2.val
                pointer = newNode
                list2 = list2.next
                
        temp = result
        result = result.next
        temp.next = None
        del(temp)
        return result
