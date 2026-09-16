N = int(input())
A = list(map(int, input().split()))
A.sort()
Alice = 0
Bob = 0

turn = 0
while A:
    if turn % 2 ==0:
        Alice += A.pop()
    else:
        Bob += A.pop()
    turn += 1
print(Alice - Bob)