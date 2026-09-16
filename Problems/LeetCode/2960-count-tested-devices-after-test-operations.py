class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for i, device in enumerate(batteryPercentages):
            if device > 0:
                tested += 1
                for j in range(i+1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j]-1)
  
            else:
                continue
        return tested