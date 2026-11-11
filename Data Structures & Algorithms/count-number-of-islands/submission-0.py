class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Have set to keep track of whether island has been discovered
        visited = set()
        count = 0
        
        # Repeat this search for every item in matrix
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # If item has been visited or it is water, ignore
                if (row, column) in visited or grid[row][column] == '0':
                    continue

                # Otherwise, we found a new island
                # Increment the count and mark neighboring land as visited
                count += 1
                self.markVisited(grid, row, column, visited)

        # Return number of islands
        return count

    def markVisited(self, grid: List[List[str]], row, column, visited) -> None:
        # Base case: Out of bounds
        if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid[0])):
            return

        # Base case: Water, so end traversal for island
        if grid[row][column] == '0':
            return

        # Base case: Already visited
        if (row, column) in visited:
            return

        # Base case: Otherwise, mark as visited
        visited.add((row, column))

        # Traverse its neighbors
        self.markVisited(grid, row - 1, column, visited)
        self.markVisited(grid, row, column - 1, visited)
        self.markVisited(grid, row + 1, column, visited)
        self.markVisited(grid, row, column + 1, visited)