from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))

best = (A[0], A[1])
for j, n in enumerate(A):
    target = -n

    resIDXLeft = bisect_left(A, target)
    resIDXRight = bisect_right(A, target)

    poss =  [resIDXLeft-1, resIDXLeft, resIDXLeft+1, resIDXRight-1, resIDXRight, resIDXRight+1]
    for i in poss:
        if i ==j: continue
        if i not in range(len(A)): continue

        diff = abs(A[i] + n)

        if diff < abs(best[0]+best[1]):
            best = (n, A[i])
print(*sorted(best))
