# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head