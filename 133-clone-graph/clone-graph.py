"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def dfs(node):
            if not node:
                return None
            elif node in mapping:
                return mapping[node]

            newNode = Node(node.val, [])
            mapping[node] = newNode

            for nei in node.neighbors:
                newNei = dfs(nei)
                newNode.neighbors.append(newNei)

            return newNode

        return dfs(node)
        