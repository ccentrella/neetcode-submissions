class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Use Kadane's algorithm twice
        # Once for max and once for min, simultaneously
        # Use min to calculate the max on the edges by removing center

        max_value = float("-inf")
        min_value = float("inf")
        current_max = 0
        current_min = 0
        total = 0
        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)

            max_value = max(current_max, max_value)
            min_value = min(current_min, min_value)

            total += num

        if max_value < 0:
            return max_value

        return max(max_value, total - min_value)