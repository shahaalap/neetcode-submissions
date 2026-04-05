class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i , j, result = 0, 0, []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            result.append(word1[i:len(word1)])

        if j < len(word2):
            result.append(word2[j:len(word2)])

        return ''.join(result)
