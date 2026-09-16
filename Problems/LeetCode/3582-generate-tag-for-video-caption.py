class Solution:
    def generateTag(self, caption: str) -> str:
        tag = []
        charLimit = 100
        shouldUpper = False
        for char in caption:
            if char == " ":
                shouldUpper = True
            if not char.isalpha():
                continue
            
            else:
                if shouldUpper:
                    tag.append(char.upper())
                    shouldUpper = False

                else:
                    tag.append(char.lower())
        if not tag: return "#"
        tag[0] = tag[0].lower()
        return ("#" + "".join(tag))[:charLimit]

            
