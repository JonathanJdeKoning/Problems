A, B = list(map(int, input().split()))
diff = B - A

H = (diff*(diff+1)) // 2
print(H - B)