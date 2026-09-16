class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()
            
            if not stack:
                ans[num] = -1
            else:
                ans[num] = stack[-1]
            stack.append(nums2[i])
        return [ans[x] for x in nums1]
        