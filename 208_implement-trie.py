class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.next = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Node('-1')

    def insert(self, word: str) -> None:
        # O(n)
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                node = Node(c)
                cur.next[idx] = node
            cur = cur.next[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        # O(n)
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                return False
            cur = cur.next[idx]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        # O(n)
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                return False
            cur = cur.next[idx]
        return True
        
