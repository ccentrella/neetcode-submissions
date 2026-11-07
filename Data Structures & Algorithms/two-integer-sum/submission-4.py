class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            difference = target - num
            
            if difference in map:
                return [map[difference], index]

            # Otherwise, add the num
            map[num] = index
