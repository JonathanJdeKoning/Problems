class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs = [log for log in logs if log.split()[-1][-1].isdigit()]
        lets = [log for log in logs if not log.split()[-1][-1].isdigit()]

        lets.sort(key = lambda x: (x[x.index(" "):], x[:x.index(" ")]))
        return lets + digs