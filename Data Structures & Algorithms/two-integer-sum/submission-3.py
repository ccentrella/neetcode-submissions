class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in differences:
                return [min(index, differences[difference]), max(index, differences[difference])]
            differences[num] = index

        # If we reach this point, our test case is invalid
        raise KeyError