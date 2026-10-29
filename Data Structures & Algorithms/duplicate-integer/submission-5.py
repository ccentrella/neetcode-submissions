class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for num in nums:
            if found.get(num):
                return True
            found[num] = True
        return False