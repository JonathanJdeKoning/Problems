def solve():
    N = int(input())
    A = list(map(int, input().split()))

    def adj(i):
        return [A[(i-1) % len(A)], A[(i+1) % len(A)]]

    ans = 1

    while len(A) != 1:
        for i in range(len(A)):
            l, r = adj(i)

            if l != r:
                ans += 1
                A.pop(i)
                break
        else:
            A.pop()
            ans += 1
            if len(A) == 1: break
            for i in range(len(A)):
                if A[i] == A[(i+1) % len(A)]:
                    A.pop(i)
                    break
    return ans    


for _ in range(int(input())):

    print(solve())