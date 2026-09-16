class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s):
            if len(s) == n*2: ans.append(s); return

            o, c = s.count("("), s.count(")")
            if o < n: dfs(s+"(")
            if o > c: dfs(s+")")
            
        dfs("(")
        return ans
