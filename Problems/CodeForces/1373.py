def solve():
    S = input()
    stack = []
    dels = 0

    for c in S:
        if not stack:
            stack.append(c)
            continue
        if stack[-1] != c:
            stack.pop()
            dels += 1
        else:
            stack.append(c)
    while len(stack) >= 2 and stack[-1] != stack[-2]:
        stack.pop()
        stack.pop()
        dels += 1

    if dels %2 == 1:
        print("DA")
    else:
        print("NET")
    

T = int(input())

for _ in range(T):
    solve()

