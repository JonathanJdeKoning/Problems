N = int(input())
A = list(map(int, input().split()))

for num in A:
    if num%2 ==0:
        if num%3 != 0 and num %5!= 0:
            exit(print("DENIED"))
print("APPROVED")
