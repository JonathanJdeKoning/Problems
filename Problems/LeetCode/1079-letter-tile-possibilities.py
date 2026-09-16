class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        allPerms = set()
        for i in range(1, len(tiles)+1):
            for perm in permutations(tiles,i):
                allPerms.add(perm)
        return len(allPerms)
