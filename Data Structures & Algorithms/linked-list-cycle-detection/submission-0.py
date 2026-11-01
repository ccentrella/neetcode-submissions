# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # To test for cycle, traverse linked list:
        # - Have a set containing visited nodes
        # - If node is already visited, return true
        # If we reach end, return false

        visited = set()
        current = head

        while current != None:
            if current in visited:
                print(current)
                print(visited)
                return True
            visited.add(current)
            current = current.next

        # If we reach here, there is no cycle
        return False