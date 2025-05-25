x,y,n = map(int, input().split())
trip, left = divmod(n,3)
print(min(x*n,trip*y+left*x ))
