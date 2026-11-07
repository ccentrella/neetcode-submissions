class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        colors = [0 for _ in range(3)]

        # Initialize the colors list
        for num in nums:
            colors[num] += 1

        # Now modify the array in place
        left = 0
        for index, count in enumerate(colors):
            for _ in range(count):
                nums[left] = index
                left += 1

        return nums