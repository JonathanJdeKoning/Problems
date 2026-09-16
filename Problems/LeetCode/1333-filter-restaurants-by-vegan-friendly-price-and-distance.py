class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        return [x[0] for x in sorted(list(filter(lambda r: r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance, restaurants)),key=lambda s: (-s[1],-s[0]))]
        