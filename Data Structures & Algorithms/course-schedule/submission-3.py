class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create hashmap to represent adjacency list
        map = {}
        for course, prerequisite in prerequisites:
            if course not in map:
                map[course] = []
            if prerequisite not in map:
                map[prerequisite] = []

            # Append item
            map[course].append(prerequisite)

        # Step 2: Traverse items
        visited = set()
        for key in map:
            if not self.dfs(numCourses, map, key, visited):
                return False

        # If we reach here, all courses can be completed
        return True

    def dfs(self, numCourses: int, map: dict[int], key: int, visited: set[int]):
        # Base case: list empty
        if map[key] == []:
            return True

        for edge in map[key]:
            # If cycle is detected, immediately return False
            if (key, edge) in visited:
                return False

            # Otherwise, add this to the set
            # If operation is not successful, immediately return False
            visited.add((key, edge))
            if not self.dfs(numCourses, map, edge, visited):
                return False
                
        # Now mark all prerequisites as completed to avoiding needing to re-process this course
        map[key] = []

        return True

            