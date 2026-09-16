class Trie:
    def __init__(self):
        self.root = {}
    def add(self, word):
        head = self.root
        for c in word:
            if c not in head:
                head[c] = {}
            head = head[c]
        head["."] = word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = list(pairwise([-1,0,1,0,-1]))
        trie = Trie()
        for word in words:
            trie.add(word)

        R, C = len(board), len(board[0])
        ans = set()
        seen = set()
        def dfs(y, x, trieNode):
            if "." in trieNode:
                ans.add(trieNode["."])
                del trieNode["."]
            
            seen.add((y,x))

            for dy, dx in directions:
                ny, nx = dy+y, dx+x
                if (ny,nx) in seen:continue
                if ny<0 or nx<0: continue
                if ny>=R or nx>=C: continue
                if board[ny][nx] not in trieNode: continue

                dfs(ny, nx, trieNode[board[ny][nx]])
            seen.discard((y,x))

        for i in range(R):
            for j in range(C):
                cell = board[i][j]
                if cell not in trie.root: continue
                dfs(i, j, trie.root[cell])

        return list(ans)
        
        
