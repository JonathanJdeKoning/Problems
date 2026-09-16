class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        mp = {}
        items.sort()
        mx = 0
        prices =[]
        for price, beauty in items:
            mx = max(mx, beauty)
            prices.append(price)
            mp[price] = mx

        for q in queries:
            low = 0
            high = len(prices)

            while low < high:
                mid = (low + high) // 2

                if prices[mid] > q:
                    high = mid
                else:
                    low = mid + 1

            if low == 0:
                ans.append(0)
            else:
                ans.append(mp[prices[low-1]])
        return ans

