class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges = defaultdict(list)
        n, m = len(heights), len(heights[0])
        visited = [[False] * m for _ in range(n)]
        result = float('inf')

        for i in range(n):
            for j in range(m):
                if i > 0:
                    edges[(i,j)].append((i - 1, j, abs(heights[i][j] - heights[i - 1][j])))
                if i < n - 1:
                    edges[(i,j)].append((i + 1, j, abs(heights[i][j] - heights[i + 1][j])))
                if j > 0:
                    edges[(i,j)].append((i, j - 1, abs(heights[i][j] - heights[i][j - 1])))
                if j < m - 1:
                    edges[(i,j)].append((i, j + 1, abs(heights[i][j] - heights[i][j + 1])))

        q = []
        q.append((0,0,0))

        while q:
            cost, i,j = heapq.heappop(q)

            if visited[i][j]:
                continue

            visited[i][j] = True

            if i == n - 1 and j == m - 1:
                result = min(cost, result)
                continue
            
            for nei, nej, c in edges[(i,j)]:
                heapq.heappush(q, (max(cost, c), nei, nej))

        return result
    



