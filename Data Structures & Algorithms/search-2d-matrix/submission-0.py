class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [char for array in matrix for char in array]
        left, right = 0, len(matrix) - 1
        while left <= right:
            index = right - left // 2
            if matrix[index] == target:
                return True
            elif matrix[index] < target:
                left = index + 1
            else:
                right = index - 1
        return False