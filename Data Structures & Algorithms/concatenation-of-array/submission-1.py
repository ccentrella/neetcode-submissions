class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums.append(nums[index])

        return nums