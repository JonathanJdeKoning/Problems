class Solution:
    def toHexspeak(self, num: str) -> str:
        mp = {"0": "O", "1":"I", "a":"A", "b": "B", "c":"C", "d":"D", "e":"E", "f":"F"}
        ans = []

        h = hex(int(num))[2:]
        for c in h:
            if c not in mp:
                return "ERROR"
            ans.append(mp[c])
        return "".join(ans)