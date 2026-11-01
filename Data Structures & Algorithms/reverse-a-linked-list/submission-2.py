# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Populate list
        array = []
        current = head

        while current:
            array.append(current.val)
            current = current.next

        # Step 2: Convert back to linked list
        head = None
        for item in array:
            head = ListNode(item, head)

        return head

        # Time: O(n)
        # Space: O(n), because we make an intermediate array