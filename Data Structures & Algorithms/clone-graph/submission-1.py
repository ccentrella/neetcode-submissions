"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # We need a way to track the nodes so that we don't add the same node twice
        # Have a hashmap mapping old_node:new_node
        # As we iterate neighbors, we will determine whether node already exists
        # If so, add to hashmap. Otherwise, use existing node
        # To add all nodes, use DFS

        if not node:
            return

        return self.createEdges(node, set(), {})

    def createEdges(self, node: 'Node', visited: set, map: {}):
        # Confirm node is in map or create a new one
        if node.val not in map:
            map[node.val] = Node(node.val)

        # If visited, return the existing node
        if node.val in visited:
            return map[node.val]

        # Otherwise, also traverse the node's outgoing edges
        visited.add(node.val)
        new_node = map[node.val]
        for neighbor in node.neighbors:
            new_neighbor = self.createEdges(neighbor, visited, map)
            new_node.neighbors.append(new_neighbor)

        # Once this has completed recursively, return the new_node
        return new_node