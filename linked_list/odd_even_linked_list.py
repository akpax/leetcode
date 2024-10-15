# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(0)
        even_head = ListNode(0)
        odd = odd_head
        even = even_head
        i = 1
        while head != None:
            if i % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            
            head = head.next 
            i += 1
        even.next = None
        odd.next = even_head.next
        return odd_head.next