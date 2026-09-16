class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        for x in paths:
            cities.add(x[0])
        return [x[1] for x in paths if x[1] not in cities][0]