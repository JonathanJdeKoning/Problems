A, B = list(map(int, input().split()))
if B==100:
    B += 1
print(B*pow(100, A))