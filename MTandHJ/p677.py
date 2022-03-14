



class MapSum:

    def __init__(self):
        self.value = 0
        self.children = dict()

    def insert(self, key: str, val: int) -> None:
        if len(key) == 0:
            self.value = val
        else:
            try:
                self.children[key[0]].insert(key[1:], val)
            except KeyError:
                child = MapSum()
                child.insert(key[1:], val)
                self.children[key[0]] = child

    def over(self):
        ans = self.value
        for child in self.children.values():
            ans += child.over()
        return ans
    
    def sum(self, prefix: str) -> int:
        if len(prefix) == 0:
            return self.over()
        else:
            try:
                return self.children[prefix[0]].sum(prefix[1:])
            except KeyError:
                return 0
