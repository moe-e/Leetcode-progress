class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        all_nums = {}
        
        for i in range(len(nums)):
            if nums[i] not in all_nums:
                all_nums[nums[i]] = 1
                
            else:
                return True
            
        return False