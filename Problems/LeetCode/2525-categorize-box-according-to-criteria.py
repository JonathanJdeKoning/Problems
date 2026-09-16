class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = len([x for x in [length, width, height] if x >= 10**4]) !=0 or length*width*height >= 10**9
        heavy = mass >= 100

        if heavy:
            if bulky: return "Both"
            return "Heavy"
        return "Bulky" if bulky else "Neither"