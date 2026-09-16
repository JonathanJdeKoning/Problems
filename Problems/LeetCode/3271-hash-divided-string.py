class Solution:
    def stringHash(self, s: str, k: int) -> str:
        from itertools import islice
        def chunk(arr_range, arr_size):
            arr_range = iter(arr_range)
            return iter(lambda: tuple(islice(arr_range, arr_size)), ())

        chunks = list(chunk(s, k))
        print(chunks)
        result = []
        for chunk in chunks:
            h = sum([ord(x)-ord("a") for x in chunk])%26
            result.append(chr(h+97))
        return "".join(result)
