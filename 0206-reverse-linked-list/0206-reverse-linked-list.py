# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        change = None
        cur = head
        
        while cur:
            next_one = cur.next
            cur.next = change
            change = cur
            cur = next_one
            
        return change
            
            