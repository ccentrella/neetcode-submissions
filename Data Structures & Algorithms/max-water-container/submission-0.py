class Solution:
    def maxArea(self, heights: List[int]) -> int:
        longest_area = 0
        longest_indices = [0,0]
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            if width * height > longest_area:
                longest_area = width * height
                longest_indices = [left, right]
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return longest_area
