class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        total = 0
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            
            
            while l < r:
                
                if nums[l] - nums[i] > diff:
                    break

                elif nums[l] - nums[i] < diff:
                    l += 1
                    
                elif nums[l] - nums[i] == diff:
                    
                    if nums[r] - nums[l] > diff:
                        r -=1

                    elif nums[r] - nums[l] < diff:
                        break
                        
                    else:
                        total +=1
                        break
                        
        return total
        