class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new = []
        for i in range(len(nums)):
            new.append(nums.pop())
        new = new[::-1]
        new = new[-(k%len(new)):]+new[:-(k%len(new))]
        for num in new:
            nums.append(num)
        