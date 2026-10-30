class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use for loop instead of for in, to prevent Exception when deleting
        # Capture current_length as the length of array
        # For each item, if the item matches val:
        # - remove item at index
        # - don't update index
        # - subtract 1 from current_length
        # Otherwise, update index by 1
        # Return current_length

        new_length = len(nums)
        index = 0
        for _ in range(len(nums)):
            # Since we move items to the end of the list, we intentionally exit before index hits end. The range will terminate after each element has been traversed exactly once.
            if nums[index] == val:
                nums[index], nums[new_length - 1] = nums[new_length - 1], nums[index]
                new_length -= 1
            else:
                index += 1

        return new_length