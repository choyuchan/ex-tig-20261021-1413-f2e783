import sys
from collections import deque


def solve(n, m, grid):
    """Return (number of islands, size of the largest island)."""
    visited = [[False] * m for _ in range(n)]
    count = 0
    largest = 0
    for sr in range(n):
        for sc in range(m):
            if grid[sr][sc] != "1" or visited[sr][sc]:
                continue
            # Iterative BFS avoids recursion limits on a 50x50 all-land map.
            count += 1
            size = 0
            visited[sr][sc] = True
            queue = deque([(sr, sc)])
            while queue:
                r, c = queue.popleft()
                size += 1
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == "1":
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            largest = max(largest, size)
    return count, largest


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2:2 + n]
    count, largest = solve(n, m, grid)
    sys.stdout.write(f"{count}\n{largest}\n")


if __name__ == "__main__":
    main()
