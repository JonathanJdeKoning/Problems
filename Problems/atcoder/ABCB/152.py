a, b = list(map(int, input().split()))


A = str(b)*a
B =  str(a) * b

print(min(A, B ))