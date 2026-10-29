class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] = True

        # If we reach this point, no duplicates exist
        return False