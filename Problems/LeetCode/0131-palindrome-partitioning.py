class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def get_partitions(s):
            # Helper function to recursively generate partitions
            def partition_helper(start, path, result):
                if start == len(s):
                    result.append(path)
                    return
                
                for i in range(start + 1, len(s) + 1):
                    partition_helper(i, path + [s[start:i]], result)

            result = []
            partition_helper(0, [], result)
            return result
        
        return [part for part in get_partitions(s) if len([x for x in part if x == x[::-1]])==len(part)]
