mp = {
    "G": "T",
    "C": "TG",
    "A": "C",
    "T": "CA"
}
mp2 = {
    "G": "CA",
    "C": "CAT",
    "A": "TG",
    "T": "TGC"
}

mp4 = {
    "G": "CATTG",
    "C": "CATTGTGC",
    "A": "TGC"
}
A = "CAT"
"""
String Length is Fibonacci
Next Iteration is the "AG"/"TC" Inverse concatenated with the current prefix of the length of the previous iteration
'A' is always preceded by 'C'
'G' is always preceded by 'T'
'CC' and 'TT' are the only doubles
"""
for _ in range(5):
    A = "".join([mp2[x] for x in A])
    print(A)

A = "CAT"

for _ in range(5):
    A = "".join([mp[x] for x in A])
    A = "".join([mp[x] for x in A])
    print(A)
    