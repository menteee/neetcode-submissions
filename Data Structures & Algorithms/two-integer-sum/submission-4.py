class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,j in enumerate(nums):
            s = target - j
            if s in hashmap:
                return [hashmap[s], i] 
            hashmap[j] = i