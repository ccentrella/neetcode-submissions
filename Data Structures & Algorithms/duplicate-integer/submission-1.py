class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integers = set()
        for num in nums:
            if num in integers:
                return True
            integers.add(num)

        # If we reach here, no duplicates exist
        return False