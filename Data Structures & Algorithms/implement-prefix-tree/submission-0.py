class PrefixTree:

    def __init__(self):
        self.nodes = {}
        self.eol = False

    def insert(self, word: str) -> None:
        cur = self
        
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = PrefixTree()
                
            cur = cur.nodes[c]

        cur.eol = True

    def search(self, word: str) -> bool:
        cur = self

        for c in word:
            if c not in cur.nodes:
                return False

            cur = cur.nodes[c]

        return cur.eol
        

    def startsWith(self, prefix: str) -> bool:
        cur = self

        for c in prefix:
            if c not in cur.nodes:
                return False

            cur = cur.nodes[c]

        return True
        
        