class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        aa = ["a"]*a
        bb = ["b"]*b
        cc = ["c"]*c
        out = []
        poss = [aa,bb,cc]
        while True:
            old = len(out)
            poss.sort(key=lambda x: len(x))
            
            for i in range(2,-1,-1):
                char = poss[i]
                if not char: continue
                choice = char[0]
                if choice == "a" and not a: continue
                if choice == "b" and not b: continue
                if choice == "c" and not c: continue

                if len(out) >= 2 and (out[-1] == choice and out[-2] == choice):
                    continue
                else:
                    if choice == "a": a-=1
                    if choice == "b": b-=1
                    if choice == "c": c-=1
                    out.append(poss[i].pop())
                    break
            if len(out) == old: break
        return "".join(out)

        