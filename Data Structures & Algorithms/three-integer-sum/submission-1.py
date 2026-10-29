class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        differences = {num:index for index, num in enumerate(nums)}
        triplets = set()
        for outer_index in range(len(nums)):
            for inner_index in range(outer_index+1, len(nums)):
                difference = 0 - nums[outer_index] - nums[inner_index]
                if difference in differences and differences[difference] not in (outer_index, inner_index):
                    triplets.add(tuple(sorted([nums[outer_index], difference, nums[inner_index]])))
        return [list(triplet) for triplet in triplets]

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)