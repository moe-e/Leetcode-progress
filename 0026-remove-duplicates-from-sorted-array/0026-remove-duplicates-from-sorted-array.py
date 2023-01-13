class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sub = 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[sub] = nums[i]
                sub += 1
                
        return sub
            