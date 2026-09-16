class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1 or bits.count(0) == len(bits): return True

        l,r = 0,1
        while True:
            a,b = bits[l],bits[r]
            l += a+1
            r += a+1


            if r == len(bits) - 1 and bits[l] == 0:
                print("a")
                return True
            if l == len(bits) - 1:
                print("b")
                return True

            if l == len(bits): return False