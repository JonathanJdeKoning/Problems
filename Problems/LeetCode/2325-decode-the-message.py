class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ","")
        lets = {" ": " "}
        curr = 97
        for c in key:
            if c not in lets:
                lets[c] = chr(curr)
                curr+=1
        new = []
        for c in message:
            new.append(lets[c])
        return "".join(new)