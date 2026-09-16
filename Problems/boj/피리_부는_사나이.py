MP = {
    "U": -1,
    "D": -2,
    "L": -3,
    "R": -4
}
mp = {
    -1: (-1,0),
    -2: (1,0),
    -3: (0, -1),
    -4: (0,1)
}
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

R, C = list(map(int, input().split()))
M = [[MP[c] for c in input()] for _ in range(R)]
ans = 0
ID = 0
dsu = DisjointSetUnion(R*C)

def getID(i,j):
    return i*C + j
for i in range(R):
    for j in range(C):
        if M[i][j] == "#": continue
        ans += 1
        y, x = i, j
        base = getID(i,j)
        while M[y][x] != "#":
            dy, dx = mp[M[y][x]]
            M[y][x] = "#"
            y += dy
            x += dx
            dsu.union(base, getID(y,x))
        dsu.union(base, getID(y,x))

print(len(dsu))

