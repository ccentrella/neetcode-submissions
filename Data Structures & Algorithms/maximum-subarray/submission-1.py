class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use Kadane's algorithm
        # For each iteration, set current to max of current and 0
        # Then set current to max of current and max

        max_value = float("-inf")
        current = 0
        for num in nums:
            current = max(num, current + num)
            max_value = max(max_value, current)

        return max_value
