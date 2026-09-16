class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)

        return len([x for x in message if x in bannedWords]) >= 2