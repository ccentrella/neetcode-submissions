class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Start by having a counter which is the current number in a row
        # In addition, have another variable that holds the max
        # If we see a one, increase counter set max to max(max, counter)
        # Otherwise, leave max alone, but reset counter to 0

        longest_range = 0
        current_range = 0
        for num in nums:
            if num == 1:
                current_range += 1
                longest_range = max(current_range, longest_range)
            else:
                current_range = 0

        return longest_range