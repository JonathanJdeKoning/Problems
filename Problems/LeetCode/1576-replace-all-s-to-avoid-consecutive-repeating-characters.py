class Solution:
    def modifyString(self, s: str) -> str:
        s = ["#"]+list(s)+["#"]
        for i,c in enumerate(s[1:-1], start=1):
            if c == "?":
                choice = ["a","b","c"]
                try: choice.remove(s[i+1])
                except:pass
                try: choice.remove(s[i-1])
                except: pass
                s[i] = choice[0]
        return "".join(s[1:-1])
                
