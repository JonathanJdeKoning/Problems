class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        seen = set()
        while q:
            currRoom = q.popleft()
            if currRoom in seen: continue
            seen.add(currRoom)
            keys = rooms[currRoom]
            for key in keys:
                if key in seen: continue
                q.append(key)

        return len(seen) == len(rooms)