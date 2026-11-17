class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Search for a cyclic graph
        # This is NOT connected, so we must run DFS or BFS on every node
        # Only process node if it has not already been visited to avoid excessive time complexity

        # Step 1: First, create a hashmap to store courses
        map = {}
        for course, prerequisite in prerequisites:
            if course not in map:
                map[course] = []
            if prerequisite not in map:
                map[prerequisite] = []

            # Now add required prerequisite for the course
            map[course].append(prerequisite)

        # Step 2: Now traverse each node
        # Once we confirm a course can be completed, remove its prerequisites
        # If we ever reach a cycle, return False

        visited = set()
        for key in map.keys():
            if not self.dfs(numCourses, map, key, visited):
                return False

        # If we reach to this point, course schedule is valid
        return True
    
    def dfs(self, numCourses: int, map: Dict[int], key: int, visited: set) -> bool:

        # Base case: No prerequisites
        if map[key] == []:
            return True

        # Base case: Cycle found
        if key in visited:
            return False

        # Add this course as visited
        visited.add(key)

        for edge in map[key]:
            if not self.dfs(numCourses, map, edge, visited):
                return False

        # Now remove from visited
        # Visited is used for finding cycles, not for avoiding traversal
        # Alternatively, we could add edges to visited
        visited.remove(key)

        # Now remove this course's prerequisites
        # This operation is used to indicate the course has already been traversed
        map[key] = []

        return True
        