class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1
        
        while digits[last] ==9:
            digits[last] = 0
            last -=1
            
            
        if last < 0 :
            digits = [1] + digits
            
        else:
            digits[last] += 1
            
        return digits
            
            
        
            
    