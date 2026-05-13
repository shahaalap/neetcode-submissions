class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        result = []

        def get_key(word):
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1

            return tuple(key)


        for st in strs:
            count = get_key(st)
            data[count].append(st)

        for key,value in data.items():
            result.append(value)

        return result