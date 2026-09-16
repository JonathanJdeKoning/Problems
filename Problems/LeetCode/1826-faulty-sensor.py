class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        if sensor1[:-1] == sensor2[:-1]: return -1

        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                if sensor1[i+1:] == sensor2[i:-1] and sensor2[i+1:] == sensor1[i:-1]:
                    return -1
                elif sensor1[i+1:] == sensor2[i:-1]:
                    return 2
                elif sensor2[i+1:] == sensor1[i:-1]:
                    return 1
                else:
                    return -1