class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        result = 0

        def subsequence(text: str) -> list[str]:
            result  = []
            def helper(i, tempSubSeq):
                if i == len(text):
                    result.append(''.join(tempSubSeq))
                    return

                #Exclude
                helper(i + 1, tempSubSeq)

                #Include
                tempSubSeq.append(text[i])
                helper(i + 1, tempSubSeq)
                tempSubSeq.pop()

            helper(0, [])
            return result

        subseqOfText1 = subsequence(text1)
        subseqOfText2 = subsequence(text2)

        for t1 in subseqOfText1:
            for t2 in subseqOfText2:
                if t1 == t2:
                    result = max(result, len(t1))

        return result
