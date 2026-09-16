class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        for i, c in enumerate(dominoes):
            if c == ".": continue
            q.append((i, c))
        ans = list(dominoes)


        while q:
            currRound = defaultdict(int)
            for _ in range(len(q)):
                i, d = q.popleft()

                if d == "L" and i != 0 and ans[i-1] == ".":
                    currRound[i-1] -= 1
                if d == "R" and i != len(dominoes) - 1 and ans[i+1] == ".":
                    currRound[i+1] += 1
            print(currRound)
            for new, d in currRound.items():
                if d == -1:
                    q.append((new, "L"))
                    ans[new] = "L"
                if d == 1:
                    q.append((new, "R"))
                    ans[new] = "R"
        return "".join(ans)