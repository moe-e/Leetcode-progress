class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            needed =target - nums[i]
            if needed in ht:
                return [i, ht[needed]]
            
            else:
                ht[nums[i]] = i
                   
            