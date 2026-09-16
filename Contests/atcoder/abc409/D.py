
def solve():
    L = int(input())
    S = input()
    idx = None
    for i in range(len(S)-1):
        if S[i+1] < S[i]:
            idx = i; break
    if idx is None: return S
    
    base = S[idx]
    end = None
    for j in range(idx, len(S)):
        if base < S[j]:
            end = j
            break
    if end is None:
        return S[:idx] + S[idx+1:] + S[idx]
    
    return S[:idx] + S[idx+1:end] + S[idx] + S[end:]

    
N = int(input())
for _ in range(N):
    print(solve())