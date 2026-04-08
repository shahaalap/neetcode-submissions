class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        result = math.inf
        prices = [math.inf] * n
        q = deque([(src, 0, k)])

        while q:
            node, cost, stop = q.popleft()

            if node == dst:
                result = min(result, cost)
                continue
            
            if stop < 0:
                continue
            

            for flight in flights:
                if flight[0] == node and prices[flight[1]] > cost + flight[2]:
                    prices[flight[1]] = cost + flight[2]
                    q.append((flight[1], cost + flight[2], stop - 1))

        if result == math.inf:
            return -1
        else:
            return result


            