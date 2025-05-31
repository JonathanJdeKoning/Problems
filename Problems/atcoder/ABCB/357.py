s = input()
up = [x for x in s if x.isupper()]
low = [x for x in s if x.islower()]

if len(up) > len(low):
    print(s.upper())
else:
    print(s.lower())
