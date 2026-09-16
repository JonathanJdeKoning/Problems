class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        g=[[2,2,2],[2,2,2],[2,2,2]]
        for i,m in enumerate(moves):g[m[0]][m[1]]=0 if i%2!=0 else 1
        for row in g:
            if row==[1,1,1]:return"A"
            if row==[0,0,0]:return"B"
        for i in range(3):
            if[x[i] for x in g]==[1,1,1]:return"A"
            if[x[i] for x in g]==[0,0,0]:return"B"
        d=[g[i][i]for i in range(3)]
        e=[g[i][-(i+1)]for i in range(3)]
        if[1,1,1]in[d,e]:return"A"
        if[0,0,0]in[d,e]:return"B"
        return"Pending"if len(moves)<9 else"Draw"


