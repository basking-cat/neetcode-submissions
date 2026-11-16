from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, visited, grid)

        return count

    def bfs(self, i, j, visited, grid):
        queue = deque()
        queue.append((i, j))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == '1':
                    visited.add((nr, nc))
                    queue.append((nr, nc))
