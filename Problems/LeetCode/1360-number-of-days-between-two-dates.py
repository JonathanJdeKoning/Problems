class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import date
        ymd = lambda d: [int(x) for x in d.split("-")]
        return abs((date(*ymd(date1))-date(*ymd(date2))).days)