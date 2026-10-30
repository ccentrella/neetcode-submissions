class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # Naive solution: Iterate over nums twice and append to a new array
        # Alternatively, iterate over nums once and append to array

        for index in range(len(nums)):
            nums.append(nums[index])

        return nums