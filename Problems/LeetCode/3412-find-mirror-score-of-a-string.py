class Solution:
    def calculateScore(self, s: str) -> int:
        alph = "abcdefghijklmnopqrstuvwxyz"
        m = {}
        for i, c in enumerate(alph):
            m[c] = alph[~i]
        marked = set()
        ms = defaultdict(list)
        ans = 0
        #print(m)
        for i, c in enumerate(s):
            ms[m[c]].append(i)
            if not ms[c]: continue
            while ms[c] and (j:=ms[c].pop()) not in marked:
                ans += i - j
                marked.add(i)
                marked.add(j)
                break
                #print(j,i, c)
        return ans           