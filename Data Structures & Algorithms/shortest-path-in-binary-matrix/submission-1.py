class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS is most efficient, since this is a shortest path problem

        # If initial item or last item is not 0, there is no clear path
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = collections.deque()
        visited = set()
        level = 1

        # Add initial item to queue
        queue.append((0, 0))

        while len(queue) > 0:

            # Keep track of the level
            for _ in range(len(queue)):
                (row, column) = queue.popleft()

                # If item meets criteria, then report current level
                if row == len(grid) - 1 and column == len(grid) - 1:
                    return level

                # Ignore path if it is out of bounds
                if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid)):
                    continue

                # Ignore cells that are visited or do not have a 0
                if (row, column) in visited or grid[row][column] != 0:
                    continue
                
                # Now mark as visited
                visited.add((row, column))

                # Add neighboring paths
                queue.append((row - 1, column))
                queue.append((row, column - 1))
                queue.append((row + 1, column))
                queue.append((row, column + 1))
                queue.append((row - 1, column - 1))
                queue.append((row - 1, column + 1))
                queue.append((row + 1, column - 1))
                queue.append((row + 1, column + 1))

            level += 1

        # If we reach here, no shortest path was found
        return -1