class Trie:
    def __init__(self):
        self.children = {}
        self.eol = False
        
class WordDictionary:
    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]

        cur.eol = True
        

    def search(self, word: str) -> bool:

        def helper(i, node):
            cur = node

            for j in range(i, len(word)):
                c = word[j]

                if c != '.':
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    for child in cur.children.values():
                        if helper(j + 1, child):
                            return True
                    return False
            return cur.eol
        return helper(0, self.root)


        
