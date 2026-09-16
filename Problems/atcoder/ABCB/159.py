

S = input()
if S != S[::-1]:
    exit(print("No"))

mid = len(S)// 2
sub = S[:mid]

if sub != sub[::-1]:
    exit(print("No"))

sub = S[mid+1:]

if sub != sub[::-1]:
    exit(print("No"))

print("Yes")