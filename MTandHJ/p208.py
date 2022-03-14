



class Trie:

    def __init__(self):
        self.active = False
        self.children = dict()

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.active = True
        else:
            try:
                self.children[word[0]].insert(word[1:])
            except KeyError:
                child = Trie()
                child.insert(word[1:])
                self.children[word[0]] = child

    def search(self, word: str) -> bool:
        if self.active and len(word) == 0: 
            return True
        try:
            return self.children[word[0]].search(word[1:])
        except (KeyError, IndexError):
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        try:
            return self.children[prefix[0]].startsWith(prefix[1:])
        except (KeyError, IndexError):
            return False




print('a'[1:] is '')