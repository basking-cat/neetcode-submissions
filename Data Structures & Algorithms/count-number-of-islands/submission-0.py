from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    count += 1
        return count

        
    def bfs(self, start_r, start_c, grid, visited):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))