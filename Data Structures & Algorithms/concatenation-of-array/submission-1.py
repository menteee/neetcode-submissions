class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans1 = []
        for a in nums:
            ans1.append(a)
        ans = nums + ans1
        return ans
        