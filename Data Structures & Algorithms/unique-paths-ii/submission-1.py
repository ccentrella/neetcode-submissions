class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Bottom up dynamic programming approach 🤖
        # The robot can only move if the place is not blocked
        # Start at bottom right and populate grid up
        # Bc there is a block, however, we need to check for a 1 each time
        # If there is a 1, that entire path becomes excluded

        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0]) # This is a rectangular array not jagged

        previous_row = [0] * column_count
        for row in range(row_count - 1, -1, -1):
            current_row = [0] * column_count

            # If last item is not blocked, set this to 1
            if row == row_count - 1 and obstacleGrid[row][-1] == 0:
                current_row[-1] = 1

            # The robot can move straight unless there is a 1 in the path
            if previous_row[-1] == 1 and obstacleGrid[row][-1] == 0:
                current_row[-1] = 1

            # Now populate the rest of the columns
            for column in range(column_count - 2, -1, -1):

                if obstacleGrid[row][column] == 0:
                    current_row[column] = previous_row[column] + current_row[column + 1]

            previous_row = current_row

        # Result will be stored in top left corner
        return previous_row[0]