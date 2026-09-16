from collections import Counter, defaultdict
def solve():
    R, C = list(map(int, input().split()))
    M = []
    mx = 0
    for i in range(R):
        row = list(map(int, input().split()))
        M.append(row)
        for j in range(C):
            cell = row[j]
            mx = max(mx, cell)
    mxPos = []

    rows = Counter()
    cols = Counter()
    for i in range(R):
        for j in range(C):
            if M[i][j] == mx:
                rows[i] += 1
                cols[j] += 1
                mxPos.append((i,j))
    if len(rows) == 1 or len(cols) == 1: return mx-1
    if len(mxPos) <= 2: return mx-1

    mainRow = 0
    mainRowCount = 0
    mainCol = 0
    mainColCount = 0
    for k, v in rows.items():
        if v > mainRowCount:
            mainRowCount = v
            mainRow = k
    for k, v in cols.items():
        if v > mainColCount:
            mainColCount = v
            mainCol = k
    
    rv = sorted(list(rows.values()))
    cv = sorted(list(cols.values()))
    #print(cv, rv, mx)
    if len(rv) != 1 and rv[-2] != 1: return mx
    if len(cv) != 1 and cv[-2] != 1: return mx
    
    if mainRowCount == 1 and mainColCount == 1:
        return mx
    elif mainRowCount == 1:
        if len(cv) == 2:
            return mx-1
        return mx
    elif mainColCount == 1:
        if len(rv) == 2:
            return mx-1
        return mx
    else:
        for y, x in mxPos:
            if y != mainRow and x != mainCol:
                return mx
        return mx-1

    

for _ in range(int(input())):
    print(solve())