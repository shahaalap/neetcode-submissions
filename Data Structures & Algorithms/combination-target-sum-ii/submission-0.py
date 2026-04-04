class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def helper(i, slate):
            if sum(slate) == target:
                result.append(slate[:])
                return
            if sum(slate) > target:
                return
            if i == len(candidates):
                return
            
                
            helper(i + 1, slate)

            k  = i
            while k < len(candidates) - 1 and candidates[k] == candidates[k + 1]:
                    k += 1

            for _ in range(k - i + 1):
                slate.append(candidates[i])

            helper(k + 1, slate)
            
            for _ in range(k - i + 1):
                slate.pop()

        helper(0, [])

        return result