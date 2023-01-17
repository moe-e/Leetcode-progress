class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        new_arr = []
        
        for i in digits:
            num+= str(i)
            
        int_num = int(num)
        int_num+=1
        
        new_num = str(int_num)
        
        for i in new_num:
            new_arr.append(int(i))
            
        return new_arr
            
            
        
            
    