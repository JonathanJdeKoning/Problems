class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = list(set([(a,min(time, b)) for a,b in clips if a <= time]))
        need = set(range(time))
        best = []
        for i in range(len(clips)):
            a,b = clips[i]
            for j in range(len(clips)):
                if i==j: continue
                x, y = clips[j]
                if a>= x and b<= y: break
            else:
                best.append([a,b])
        if not best: return -1
        
        best.sort()
        last = best[0]
        ans = 2
        for i in range(1, len(best)-1):
            need -= set(range(*last))
            if last[1] >= best[i+1][0]: continue
            last = best[i]
            ans += 1
        need -= set(range(*last))
        need -= set(range(*best[-1]))
        
        return min(len(best), ans) if not need else -1


                