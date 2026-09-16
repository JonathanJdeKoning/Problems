class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)
        if s == "0": return 0
        if "-" not in s:
            digs = sorted([int(x) for x in s])
            zs = digs.count(0)
            digs = [x for x in digs if x != 0]
            ans = []
            ans.append(digs[0])
            ans.extend([0]*zs)
            ans.extend(digs[1:])
            return int("".join([str(x) for x in ans]))
        else:
            digs = sorted([int(x) for x in s if x != "-"], reverse = True)
            return -int("".join([str(x) for x in digs]))
