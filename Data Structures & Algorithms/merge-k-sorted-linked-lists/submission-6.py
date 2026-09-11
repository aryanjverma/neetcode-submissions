# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def printList(self, l):
        s = ""
        while l:
            s += (str(l.val) + ",")
            l = l.next
        print(s)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        for i in range(len(lists) - 2, - 1, - 1):
            if not lists[i]:
                lists[i] = lists[i + 1]
                continue
            if not lists[i + 1]:
                continue
            if lists[i].val > lists[i + 1].val:
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
            curr = lists[i]
            while curr.next and lists[i + 1]:
                if curr.next.val > lists[i + 1].val:
                    temp = curr.next
                    curr.next = lists[i + 1]
                    lists[i + 1] = lists[i + 1].next
                    curr = curr.next
                    curr.next = temp
                else:
                    curr = curr.next
            if not curr.next:
                curr.next = lists[i + 1]
            
        return lists[0]