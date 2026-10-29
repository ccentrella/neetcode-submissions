class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            current = nums[index]
            if current == target:
                return index
            elif current < nums[right] and target < current:
                right = index - 1
            else:
                left = index + 1
        return target_index