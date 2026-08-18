class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        num, maxcount = 0,0
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
            num = n if hashmap[n]>maxcount else num
            maxcount = max(hashmap[n], maxcount)
        return num

