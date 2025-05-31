a,b,c,d,e,f = map(int, input().split())
g,h,i,j,k,l = map(int, input().split())


if ((g>=d and j>=d) or (g<=a and j<=a)) or ((h>=e and k>=e) or (h<=b and k<=b)) or ((i>=f and l>=f) or (i<=c and l<=c)):
    print("No")
else:
    print("Yes")
