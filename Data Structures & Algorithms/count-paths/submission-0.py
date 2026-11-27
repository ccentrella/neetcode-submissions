class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom up dynamic programming approach
        # Start at bottom right of grid and populate row by row
        # Once we get to top left left, return value

        # Outer loop
        previous_row = [0] * n
        for row in range(m - 1, -1, -1):

            # Populate columns
            current_row = [0] * n
            current_row[-1] = 1 # There is always one path straight down
            for column in range(n - 2, -1, -1):
                current_row[column] = previous_row[column] + current_row[column + 1]
            
            previous_row = current_row

        return previous_row[0]