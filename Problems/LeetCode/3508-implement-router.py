from collections import deque, defaultdict
from typing import List
from sortedcontainers import SortedList

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.inRouter = set()
        self.packets = deque()
        self.destinations = defaultdict(SortedList)

    def _remove_oldest_packet(self) -> None:
        oldest_packet = self.packets.popleft()
        self.inRouter.discard(oldest_packet)

        timestamp, _, destination = oldest_packet
        self.destinations[destination].discard(timestamp)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (timestamp, source, destination)

        if packet in self.inRouter:
            return False

        if len(self.packets) == self.limit:
            self._remove_oldest_packet()

        self.packets.append(packet)
        self.inRouter.add(packet)
        self.destinations[destination].add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packets:
            return []

        timestamp, source, destination = self.packets.popleft()

        self.inRouter.discard((timestamp, source, destination))
        self.destinations[destination].discard(timestamp)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destinations[destination]

        left_index = timestamps.bisect_left(startTime)
        right_index = timestamps.bisect_right(endTime)

        return right_index - left_index