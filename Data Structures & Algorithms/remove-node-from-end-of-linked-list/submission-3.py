# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            if not head.next:
                return None
            temp = head
            while temp.next and temp.next.next:
                temp = temp.next
            temp.next = None
            return head
        else:
            count = 0
            temp = head
            while temp:
                temp = temp.next
                count += 1
            if n == count:
                return head.next
            trail = head
            curr = head.next
            for i in range(count - n - 1):
                trail = trail.next
                curr = curr.next
            trail.next = curr.next
            return head