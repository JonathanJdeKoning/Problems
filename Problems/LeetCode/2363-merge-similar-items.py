class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = defaultdict(int)
        for item in items1+items2:
            items[item[0]] += item[1]
        return sorted(items.items(), key=lambda k: k[0])
