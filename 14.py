from collections import deque


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]



def num_islands_dfs(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    import copy
    grid_copy = copy.deepcopy(grid)

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == 1:
                count += 1

    return count


def num_islands_dfs_safe(original_grid):
    if not original_grid or not original_grid[0]:
        return 0

    rows, cols = len(original_grid), len(original_grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or original_grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if original_grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count


def num_islands_bfs_safe(original_grid):
    if not original_grid or not original_grid[0]:
        return 0

    rows, cols = len(original_grid), len(original_grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if original_grid[r][c] == 1 and not visited[r][c]:
                count += 1
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and
                                original_grid[nr][nc] == 1 and not visited[nr][nc]):
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    return count


print("Исходная матрица:")
for row in grid:
    print(row)

print("\nКоличество островов (DFS):", num_islands_dfs_safe(grid))
print("Количество островов (BFS):", num_islands_bfs_safe(grid))