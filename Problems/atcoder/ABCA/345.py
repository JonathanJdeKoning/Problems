s = input()
if "=" not in s:print("No");exit(0)
if s[0]=="<" and s[-1] == ">" and len([x for x in s[1:-1] if x!="="])==0:print("Yes")
else:
    print("No")
