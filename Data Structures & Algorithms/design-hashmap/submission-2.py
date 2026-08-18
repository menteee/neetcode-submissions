class MyHashMap:

    def __init__(self):
        self.set1 = []

    def put(self, key: int, value: int) -> None:
        for obj in self.set1:
            if obj[0] == key:
                obj[1] = value
                return

        self.set1.append([key, value])

    def get(self, key: int) -> int:
        for obj in self.set1:
            if key == obj[0]:
                return obj[1]
           
        return -1


    def remove(self, key: int) -> None:
        for obj in self.set1:
            if key == obj[0]:
                self.set1.remove(obj)
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)