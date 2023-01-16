class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        first = []
        possible = []
        
        for i in range(len(nums)):
            if nums[i] in first:
                continue
            first.append(nums[i])
            
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                ThreeSum = nums[i] + nums[l] + nums[r]
                
                if ThreeSum > 0:
                    r-=1
                elif ThreeSum < 0:
                    l+=1
                    
                else:
                    possible.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
                    
        return possible
                    
                
                    
            
        
        