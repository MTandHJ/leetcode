

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            # 不存在，不包含前缀，返回空指针
            if not node.children[ch]:
                return None 
            # 存在，移动到下一个子节点
            node = node.children[ch]
        return node
    
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            # 不存在，创建一个
            if not node.children[ch]:
                node.children[ch] = Trie()
            # 存在，则移动到下一个
            node = node.children[ch]
        node.isEnd = True
    
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
    