class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i, c in enumerate(time):
            if c == "?":
                if i == 0:
                    try:
                        if int(time[1]) > 3:
                            time[0] = "1"
                        else:
                            time[0] = "2"
                    except:
                        time[0] = "2"
                    
                if i == 1:
                    if time[0] != "2":
                        time[1] = "9"
                    else:
                        time[1] = "3"
                if i == 3:
                    time[3] = "5"
                if i == 4:
                    time[4] = "9"
            else:
                pass
        return "".join(time)