class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def c2m(c):
            return morse[ord(c)-97]
        tot = []
        for word in words:
            mo = []
            for c in word:
                mo.append(c2m(c))
            tot.append("".join(mo))
        return len(set(tot))