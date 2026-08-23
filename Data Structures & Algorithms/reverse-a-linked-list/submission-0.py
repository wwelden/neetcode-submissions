# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        pointer = head.next
        newList = ListNode(head.val, None)
        while pointer != None:
            newNode = ListNode(pointer.val, newList)
            pointer = pointer.next
            newList = newNode
        
        return newList

