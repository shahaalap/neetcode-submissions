class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = sum(piles) // h
        if start == 0:
            return 1

        def helper(rate):
            hours = 0
            for i in piles:
                if i <= rate:
                    hours += 1
                else:
                    hours += math.ceil(i / rate)

                if hours > h:
                    return False
                    break

            return True

        i = start
        j = max(piles) + 1

        result = None
        while i <= j:
            mid = i + (j - i)//2
            if not helper(mid):
                i = mid + 1
            else:
                result = mid
                j = mid - 1
                

        return result