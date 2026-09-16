class Solution:
    def countAndSay(self, n: int) -> str:
        return "".join([str(len(list(v)))+str(list(k)[0]) for k,v in groupby(self.countAndSay(n-1))]) if n!=1 else "1"
        
            