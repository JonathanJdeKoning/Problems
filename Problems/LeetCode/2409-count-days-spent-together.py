class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import date
        aliceArriveMonth,aliceArriveDay = [int(x) for x in arriveAlice.split("-")]
        aliceLeaveMonth,aliceLeaveDay = [int(x) for x in leaveAlice.split("-")]
        bobArriveMonth,bobArriveDay = [int(x) for x in arriveBob.split("-")]
        bobLeaveMonth,bobLeaveDay = [int(x) for x in leaveBob.split("-")]


        aliceStart = date(2023, aliceArriveMonth, aliceArriveDay)
        aliceEnd = date(2023, aliceLeaveMonth, aliceLeaveDay)
        bobStart = date(2023, bobArriveMonth, bobArriveDay)
        bobEnd = date(2023, bobLeaveMonth, bobLeaveDay)
        delta = timedelta(days=1)

        aliceDates = []
        bobDates = []
        while aliceStart <= aliceEnd:
            aliceDates.append(aliceStart.isoformat())
            aliceStart += delta

        while bobStart <= bobEnd:
            bobDates.append(bobStart.isoformat())
            bobStart += delta
        return len([x for x in aliceDates if x in bobDates])