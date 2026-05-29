class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights) - 1, len(heights[0]) - 1
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minheap  = []
        heapq.heappush(minheap, (0, 0,0))
        visited = [[False] * (m + 1) for _ in range(n + 1)]

        while len(minheap):
            prevh, nodex, nodey = heapq.heappop(minheap)

            if visited[nodex][nodey]:
                continue

            visited[nodex][nodey] = True

            if nodex == n and nodey == m:
                return prevh
            
            for nei,ney in neighbors:
                x = nodex + nei
                y = nodey + ney

                if x < 0 or x > n or y < 0 or y > m:
                    continue

                heapq.heappush(minheap, (max(prevh, abs(heights[x][y] - heights[nodex][nodey])),x,y))
            
