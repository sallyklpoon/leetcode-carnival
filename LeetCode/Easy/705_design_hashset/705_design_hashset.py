from collections import deque

class MyHashSet:

    def __init__(self):
        self.set = []
        self.empty = deque()

    def add(self, key: int) -> None:
        if key not in self.set:
            if self.empty:
                i = self.empty.popleft()
                self.set[i] = key
                return
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            i = self.set.index(key)
            self.set[i] = None
            self.empty.append(i)

    def contains(self, key: int) -> bool:
        for item in self.set:
            if item == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
