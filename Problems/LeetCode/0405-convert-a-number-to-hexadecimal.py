class Solution:
    def toHex(self, num: int) -> str:
        if num ==0: return "0"
        def tohex(val, nbits):
            return hex((val + (1 << nbits)) % (1 << nbits))
        return (tohex(num, 32).lstrip('0x'))