class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start += len(distance)
        destl = destination+ len(distance)
        destfl = destination
        destr = destination + len(distance)
        destfr = destr + len(distance)
        distance*=3
        
        distr = math.inf
        distl = math.inf
        distfr = math.inf
        distfl = math.inf
        if destr >= start:
            distr = sum(distance[start:destr])
        if destl <= start:
            distl = sum(distance[destl:start])
        distfl = sum(distance[destfl:start])
        distfr = sum(distance[start:destfr])
        return min([distl, distr,distfr, distfl])