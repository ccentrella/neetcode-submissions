class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Fixed sliding window, with k distance between left and right pointers

        window = set()
        left = 0
        for right in range(len(nums)):
            
            if nums[right] in window:
                return True

            window.add(nums[right])

            # Increment only once the window has been filled
            if right - left == k:
                window.remove(nums[left])
                left += 1


        # If we reach here, there are no matches
        return False

