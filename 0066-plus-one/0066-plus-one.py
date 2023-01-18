class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1
        
        while digits[last] ==9:
            digits[last] = 0
            
            if last == 0:
                return [1] + digits
            
            last -=1
            
        digits[last] +=1
        return digits
            
            
        
            
    