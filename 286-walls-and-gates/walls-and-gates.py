class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    newr = r + dr
                    newc = c + dc

                    if newr in range(rows) and newc in range(cols) and rooms[newr][newc] == 2147483647:
                        queue.append((newr, newc))
                        rooms[newr][newc] = step

            step += 1
        