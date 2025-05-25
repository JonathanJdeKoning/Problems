h, m = 21,0

m = int(input())
if m >= 60:
    h += 1
    m = m-60
print(f"{h}:{str(m).zfill(2)}")
