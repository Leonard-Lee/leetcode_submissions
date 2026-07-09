class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [0] * (n + 1)

        # find its parent
        def find(node: int) -> int:
            if node != parents[node]:
                parents[node] = find(parents[node])

            return parents[node]

        def union(n1: int, n2: int) -> bool:
            p1 = find(n1)
            p2 = find(n2)

            # they cannot be unioned because they have the same root
            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p2] += 1

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []

        