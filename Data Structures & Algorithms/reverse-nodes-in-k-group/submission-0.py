# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        temp = head
        answer = ""
        while temp:
            answer += str(temp.val)
            answer += ","
            temp = temp.next
        print(answer)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        end = head
        for _ in range(k):
            if not end:
                return head
            end = end.next
        curr = head
        prev = self.reverseKGroup(end, k)
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
        return prev
        