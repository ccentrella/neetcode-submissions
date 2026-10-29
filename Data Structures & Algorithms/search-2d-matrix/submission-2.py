class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find correct row
        left, right = 0, len(matrix) - 1
        while left <= right:
            index = (left + right) // 2
            left_column, right_column = matrix[index][0], matrix[index][-1]
            if left_column <= target <= right_column:
                break;
            elif left_column < target:
                left = index + 1
            else:
                right = index - 1

        # Now find correct column
        row = (left + right) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            index = (left + right) // 2
            if matrix[row][index] == target:
                return True
            elif matrix[row][index] < target:
                left = index + 1
            else:
                right = index - 1
        
        # If we reach here, item cannot be found
        return False