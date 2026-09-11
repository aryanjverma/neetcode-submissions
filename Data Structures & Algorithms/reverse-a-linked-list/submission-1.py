# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        tail = None
        while curr:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
        return tail