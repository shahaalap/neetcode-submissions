class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1CharCount = Counter(s1)
        s2CharCount = {}

        n = len(s1)
        i, j = 0, 0
        while j < n - 1:
            if s2[j] in s2CharCount:
                s2CharCount[s2[j]] += 1
            else:
                s2CharCount[s2[j]] = 1

            j += 1

        while j < len(s2):
            if s2[j] in s2CharCount:
                s2CharCount[s2[j]] += 1
            else:
                s2CharCount[s2[j]] = 1

            if s1CharCount == s2CharCount:
                return True
            
            s2CharCount[s2[i]] -= 1
            if s2CharCount[s2[i]] == 0:
                del s2CharCount[s2[i]]

            
            i += 1
            j += 1

        return False