N = int(input())
digsum = sum(int(x) for x in str(N))
if N%digsum ==0 :
    print("Yes")
else:
    print("No")