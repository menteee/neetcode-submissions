class MyHashSet():

    def __init__(self):
        self.set1 = []

    def add(self,i) -> None:
        if i not in self.set1:
            self.set1.append(i)
        

    def remove(self, i) -> None:
        if i in self.set1:
            self.set1.remove(i)
        

    def contains(self, i) -> bool:
        if i in self.set1:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)