class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        
        for i in range(len(nums)):
            if nums[i] not in ht:
                ht[nums[i]] = 1
                
            else:
                ht[nums[i]] += 1
        
        res = nums[0]
        
        for key,val in ht.items():
            if val > ht[res]:
                res = key
                
        return res
            
        