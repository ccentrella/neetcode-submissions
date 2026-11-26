class Solution:
    def rob(self, nums: List[int]) -> int:
        # For each house, we can either rob the house or not rob it
        # If we do not rob it, our max so far will be all of the houses before it (n - 1)
        # But if we do rob it, it will be the houses earlier than one house before it (n - 2) + the current house.

        # Keep track of max value we can rob in an array
        # We will use this array to pull the right amounts
        # Alternatively, we can use two variables

        if len(nums) == 1:
            return nums[0]

        # First, set our initial values
        second_last, last = nums[0], max(nums[0], nums[1])
        for index in range(2, len(nums)):
            house = nums[index]
            temp = last
            last = max(second_last + house, temp)
            second_last = temp

        return last