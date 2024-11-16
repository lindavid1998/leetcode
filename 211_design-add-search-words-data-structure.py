class Node:
    def __init__(self, char):
        self.next = [None] * 26
        self.is_end = False
        self.char = char

class WordDictionary:

    def __init__(self):
        self.root = Node('-1')

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = Node(c)
            cur = cur.next[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node

            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    # handle wildcard
                    for nxt in cur.next:
                        if nxt and dfs(j + 1, nxt):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not cur.next[idx]:
                        return False
                    cur = cur.next[idx]
            
            return cur.is_end
        
        return dfs(0, self.root)


class Node:

    def __init__(self):
        self.next = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = Node()
            cur = cur.next[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            if word[i] == '.':
                for nxt in node.next:
                    if nxt and dfs(nxt, i + 1):
                        return True
                return False

            idx = ord(word[i]) - ord('a')
            print(word[i])
            if node.next[idx]:
                return dfs(node.next[idx], i + 1)
            
            
            return False
        
        return dfs(self.root, 0)

