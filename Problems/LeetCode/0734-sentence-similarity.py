class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        mp = defaultdict(set)

        for a, b in similarPairs:
            mp[a].add(b)
            mp[b].add(a)

        for a,b in zip(sentence1, sentence2):
            if a == b: continue
            if b in mp[a]: continue
            return False
        return True