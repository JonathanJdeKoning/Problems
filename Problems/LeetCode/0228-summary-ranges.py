class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out =[]
        if not nums: return []
        start = nums[0]
        toadd = [start, start]
        nums.append("YOOHOOO")
        for num in nums[1:]:
            if num == start+1:
                toadd[1] = num
            else:
                if toadd[0] == toadd[1]:
                    out.append(str(toadd[0]))
                else:
                    out.append("->".join([str(x) for x in toadd]))
                toadd = [num,num]

            start = num
        return out

