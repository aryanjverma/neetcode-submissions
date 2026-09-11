# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, node):
        temp = node
        answer = ""
        while temp:
            answer += str(temp.val)
            answer += ","
            temp = temp.next
        print(answer)
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        def reverseList(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        temp = head
        for i in range((length - 1) // 2):
            temp = temp.next
        temp.next = reverseList(temp.next)
        middle = temp.next
        temp.next = None
        
        front = head
        while middle:
            temp = front.next
            front.next = middle
            temp2 = middle.next
            middle.next = temp
            front = temp
            middle = temp2
