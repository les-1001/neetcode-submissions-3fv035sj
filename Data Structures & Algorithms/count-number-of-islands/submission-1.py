class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        island = 0
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        row, col = len(grid), len(grid[0]) 

        def bfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for i, j in directions:
                    i += r
                    j += c
                    if (i, j) not in seen and i in range(row) and j in range(col) and grid[i][j] == "1":
                        seen.add((i, j))
                        q.append((i, j))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in seen:
                    print(seen)
                    bfs(r, c)
                    island += 1
                    print(island)
        return island