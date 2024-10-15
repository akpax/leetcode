# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = 0

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None

        while curr:
            # curr.next = prev
            # prev = curr
            # curr = curr.next
            curr.next, prev, curr = prev, curr, curr.next 
        
        print(prev.val)
        while prev:
            max_val = max(max_val, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return max_val
        