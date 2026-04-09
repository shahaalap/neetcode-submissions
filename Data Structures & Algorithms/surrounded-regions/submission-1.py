class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        m,n = len(board), len(board[0])
        nei = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not (i ==0 or i == m - 1) and not (j == 0 or j == n - 1):
                    continue

                if board[i][j] == 'O':
                    q.append((i,j))
                    visited[i][j] = True


        while q:
            i,j = q.popleft()
            board[i][j] = 'S'
            
            for ni,nj in nei:
                if i + ni < 0 or i + ni >= m or j + nj < 0 or j + nj >= n:
                    continue

                if board[i + ni][j + nj] == 'O' and not visited[i + ni][j + nj]:
                    visited[i + ni][j + nj] = True
                    q.append((i + ni, j + nj))

        

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'