class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Two basic operations
        # First, change all elements before last
        # Then manually change last to -1

        # Naive approach:
        # O(n^2) time, constant space
        # We can just for each item, go through the other items to the right and find the largest one
        # Alternative, we can use a two pointers solution?

        for index, item in enumerate(arr):
            longest_to_right = 0
            for inner_index in range(index + 1, len(arr)):
                longest_to_right = max(longest_to_right, arr[inner_index])
            arr[index] = longest_to_right

        # Update last one manually
        arr[-1] = -1

        return arr

        # Space: Constant, in-place
        # Time: O(n^2)