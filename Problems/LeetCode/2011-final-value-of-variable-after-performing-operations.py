class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = 0
        n += len([x for x in operations if "+" in x])
        n -= len([x for x in operations if "-" in x])
        return n
