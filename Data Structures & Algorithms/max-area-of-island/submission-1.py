class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # If island has not been visited, then traverse this to mark parts of island as visited.
        # While doing this traversal, keep track of the count.
        # We will perform a max operation on this and the existing count.

        max_area = 0
        visited = set()

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # We only need to traverse previously unvisited islands
                if grid[row][column] == 1 and (row, column) not in visited:
                    count = self.markVisited(grid, row, column, visited)
                    max_area = max(max_area, count)

        # If there is no island, this will be zero without additional code
        return max_area

    def markVisited(self, grid: List[List[int]], row, column, visited) -> int:
        # Base case: Out of bounds
        if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid[0])):
            return 0

        # Base case: Water
        if grid[row][column] == 0:
            return 0

        # Base case: Already visited
        if (row, column) in visited:
            return 0

        # Add to visited so this doesn't get processed again
        visited.add((row, column))

        # Add the count of this node
        count = 1

        # Now add its neighbors recursively
        count += self.markVisited(grid, row-1, column, visited)
        count += self.markVisited(grid, row, column-1, visited)
        count += self.markVisited(grid, row+1, column, visited)
        count += self.markVisited(grid, row, column+1, visited)

        return count
