class FileSystem:

    def __init__(self):
        self.seen = {"":None}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.seen: return False
        parent = "/".join(path.split("/")[:-1])
        if parent not in self.seen: return False
        self.seen[path] = value
        return True


    def get(self, path: str) -> int:
        if path not in self.seen: return -1
        return self.seen[path]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)