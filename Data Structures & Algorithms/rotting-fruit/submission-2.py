class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Zero fresh fruits means that we need way to find the shortest path between all fruit.
        
        # Step 1: Add all rotten fruits to queue, while taking note of number of fresh fruits
        fresh_fruit_count = 0
        queue = collections.deque()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    fresh_fruit_count += 1
                elif grid[row][column] == 2:
                    queue.append((row, column))

        # Step 2: Use BFS to find the shortest path starting with the rotten fruit, until all fruit are hit
        visited = set()
        total_minutes = 0
        while len(queue) > 0:
            did_rotten = False
            for _ in range(len(queue)):
                row, column = queue.popleft()

                # Ensure the space isn't out of bounds
                if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid[0])):
                    continue

                # Ensure the fruit exists and hasn't been visited
                if grid[row][column] == 0 or (row, column) in visited:
                    continue

                # Make the fruit frotten
                # This conditional is needed to avoid decrementing fresh fruit counter on first iteration
                visited.add((row, column))
                if grid[row][column] == 1:
                    fresh_fruit_count -= 1
                    grid[row][column] = 2
                    did_rotten = True

                # Now add its nearest fruit to rot too
                queue.append((row-1, column))
                queue.append((row, column-1))
                queue.append((row+1, column))
                queue.append((row, column+1))

            if did_rotten:
                total_minutes += 1

        # Step 3: If there are no fresh fruits remaining, return number of minutes; else, -1
        return total_minutes if fresh_fruit_count == 0 else -1