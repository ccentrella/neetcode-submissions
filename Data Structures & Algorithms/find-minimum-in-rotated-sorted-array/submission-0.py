class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')
        left, right = 0, len(nums) - 1
        while left < right:
            index = (left + right) // 2
            current = nums[index]
            minimum = min(minimum, current)
            if current < nums[index - 1]:
                return minimum
            elif current >= nums[index - 1]:
                left = index + 1
            else:
                right = index -1
        return minimum