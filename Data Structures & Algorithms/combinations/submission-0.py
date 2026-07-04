class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(i, output):
            nonlocal result
            
            if len(output) == k:
                result.append(output[:])
                return

            if i > n:
                return

            #include
            output.append(i)
            helper(i + 1, output)
            output.pop()

            #exclude
            helper(i + 1, output)

        helper(1, [])
        return result