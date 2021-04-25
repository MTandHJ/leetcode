"""
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xh377h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# first time
# 太蠢啦，这里用1080ms呜呜
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.keys = []
        self.hashtable = []


    def add(self, key: int) -> None:
        if key in self.hashtable:
            pass
        else:
            self.hashtable.append(key)


    def remove(self, key: int) -> None:
        if key in self.hashtable:
            self.hashtable.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hashtable


# 学习别人，使用课本上知识搞的
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.keys = []
        self.hashtable = [[] for _ in range(1009)]

    def hashkey(self, key):
        return key % 1009

    def add(self, key: int) -> None:
        j = self.hashkey(key)
        if key in self.hashtable[j]:
            pass
        else:
            self.hashtable[j].append(key)

    def remove(self, key: int) -> None:
        j = self.hashkey(key)
        if key in self.hashtable[j]:
            self.hashtable[j].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        j = self.hashkey(key)
        if key in self.hashtable[j]:
            return True
        else:
            return False
