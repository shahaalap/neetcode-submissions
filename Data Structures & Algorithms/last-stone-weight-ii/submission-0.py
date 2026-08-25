class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort(reverse = True)

        prev = 0
        for stone in stones:
            prev = abs(stone - prev)
        
        return prev