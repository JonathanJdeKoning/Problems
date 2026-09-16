class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = dict(Counter(words))
        sorted_dict = sorted(count.items(), key=lambda x:(-x[1], x[0]))
        print(sorted_dict)
        return [x[0] for x in sorted_dict[:k]]