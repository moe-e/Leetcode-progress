class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1
        
        if digits[last] < 9:
            digits[last] +=1
            return digits
        
        while digits[last] == 9:
            if last == 0 and digits[last] == 9:
                digits[last] = 1
                digits.append(0)
                return digits
                
            if digits[last - 1] == 9:
                digits[last] = 0
                last -=1
                
            elif digits[last - 1] < 9:
                digits[last] = 0
                digits[last - 1] += 1
                return digits
                
                
            
           
        return digits
            
        
            
    