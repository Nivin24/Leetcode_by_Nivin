# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        curr = head
        slow = curr
        fast = curr
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        prev = None

        
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node

        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
        