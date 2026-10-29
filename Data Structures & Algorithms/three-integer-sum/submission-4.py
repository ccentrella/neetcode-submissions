class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)
        for index, num in enumerate(nums):
            left, right = index + 1, len(nums) - 1
            difference = 0 - num
            while left < right:
                if nums[left] + nums[right] == difference:
                    triplets.add(tuple([nums[index], nums[left], nums[right]]))
                    left += 1; right -= 1
                elif nums[left] + nums[right] < difference:
                    left += 1
                else:
                    right -= 1
        return [list(triplet) for triplet in triplets]