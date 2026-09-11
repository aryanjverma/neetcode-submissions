# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 and l2:
            added = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            curr.next = ListNode(val = added)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            added = (l1.val + carry) %   10
            carry = (l1.val + carry) // 10
            curr.next = ListNode(val = added)
            curr = curr.next
            l1 = l1.next
        while l2:
            added = (l2.val + carry) %   10
            carry = (l2.val + carry) // 10
            curr.next = ListNode(val = added)
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(val = carry)
        return head.next
