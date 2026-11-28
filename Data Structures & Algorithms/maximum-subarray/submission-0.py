class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use Kadane's algorithm
        # For each iteration, set current to max of current and 0
        # Then set current to max of current and max

        max_value = float("-inf")
        current = max_value
        for num in nums:
            # Must happen in this order

            # First, if prevent running total is negative, reset to 0
            current = max(current, 0)

            # Then add current one. This is required for line 18
            current += num

            # Now update match
            max_value = max(max_value, current)

        return max_value
