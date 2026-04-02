class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = defaultdict(list)
        outdegrees = defaultdict(list)
        q = deque()
        visited = [False] * numCourses
        result = []

        for c, d in prerequisites:
            indegrees[c].append(d)
            outdegrees[d].append(c)

        for c in range(numCourses):
            if len(indegrees[c]) == 0:
                q.append(c)

        if not q:
            return result

        while q:
            node = q.pop()

            visited[node] = True
            result.append(node)

            for dep in outdegrees[node]:
                 if all([visited[ind] for ind in indegrees[dep]]) and not visited[dep]:
                    q.append(dep)

        if not all(visited):
            return []
            
        return result

        
        

                


