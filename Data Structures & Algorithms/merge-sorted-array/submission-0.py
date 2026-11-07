class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Perform merge operation on these two halves
        # Essentially this is second part of merge sort
        # In this case, the recursive part is done and we need to merge these

        # Loop over remaining elements via outer loop
        right = m
        while right < len(nums1):
            # Start inner loop to swap until list is sorted
            left = right
            item = nums2[right - m]
            nums1[left] = item

            while left > 0 and item < nums1[left-1]:
                nums1[left-1], nums1[left] = nums1[left], nums1[left-1]
                left -= 1

            right += 1

        # Once we arrive here, our array is sorted
        return nums1