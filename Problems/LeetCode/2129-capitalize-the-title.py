class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def newtitle(word):
            if len(word) <3:
                return word.lower()
            return word.title()
        return " ".join(map(newtitle, title.split()))