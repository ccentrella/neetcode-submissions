# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use previous pointer and current pointer
        # Previous pointer will point to last item, which is already in order
        # Current point will post to current item, which is not in order
        # On each iteration, set current.next to previous pointer, and use the previous next for current

        previous = None
        current = head

        while current != None:
            next = current.next
            current.next = previous

            previous = current
            current = next

        return previous