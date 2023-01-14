class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(numbers)):            
            x = target - numbers[i]
            
            if x in ht:
                return [min(i+1, ht[x]+1), max(i+1, ht[x]+1)]
                           
            if numbers[i] not in ht:
                ht[numbers[i]] = i
                
            
            
                
            