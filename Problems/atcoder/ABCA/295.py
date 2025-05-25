n = int(input())
words = set(input().split())
eng = ["and","not","that","the","you"]
for e in eng:
    if e in words:
        print("Yes");break
else:
    print("No")
