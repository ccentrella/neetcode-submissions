# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Solution 1:
# Repurpose head pointer as second pointer
# This is not maintainable, but doing as a way to show two pointers is not technically needed when you include the head.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # There is no previous pointer, so we can't start on end and work our way up
        # Start at head and traverse linked list
        # While traversing, move head to current and set next pointer to the previous head

        # Base case: Less than two elements, so there is nothing to reverse
        if head is None or head.next is None:
            return head

        # We must also set the head.next to null or we will have a weird infinite loop
        current = head.next
        head.next = None

        while current != None:
            next = current.next
            current.next = head
            head = current
            current = next

        return head
