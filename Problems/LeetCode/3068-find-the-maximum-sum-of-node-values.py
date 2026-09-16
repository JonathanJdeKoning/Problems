class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        n: int = len(nums)
        deltas: list[int] = [(nums[i] ^ k) - nums[i] for i in range(n)]  # represents how will change number after XOR
        deltas.sort(reverse=True)
        res: int = sum(nums)

        for start_ind in range(0, n - 1, 2):
            changing_delta: int = deltas[start_ind] + deltas[start_ind + 1]  # showing whether if would be beneficial if we XOR this two nodes 
            if changing_delta > 0:
                res += changing_delta
            else:
                break

        return res