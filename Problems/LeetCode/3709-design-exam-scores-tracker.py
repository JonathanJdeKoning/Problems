class ExamTracker:

    def __init__(self):
        self.pref = {0:0}
        self.allTimes = [0]
        self.total = 0

    def record(self, time: int, score: int) -> None:
        self.total += score
        self.pref[time] = self.total
        self.allTimes.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        bestStartIDX = bisect_left(self.allTimes, startTime) - 1
        bestEndIDX = bisect_right(self.allTimes, endTime) - 1

        bestStart = self.allTimes[bestStartIDX]
        bestEnd = self.allTimes[bestEndIDX]

       # print(f"AllTimes: {self.allTimes}")
        #print(f"Time: [{startTime} - {endTime}]")
        #print(f"BestStart: {bestStart}")
        #print(f"BestEnd: {bestEnd}")
        return self.pref[bestEnd] - self.pref[bestStart]



# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)