class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        res = []
        
        for i in nums:
            if i not in ht:
                ht[i] = 1
                
            else:
                ht[i] += 1
                
        
        
        i = 0

        while i < k:
            max_val = False
            for key,val in ht.items():
                if max_val == False:
                    max_val = val
                    max_key = key
                
                if val > max_val:
                    max_val = val
                    max_key = key
                    

            res.append(max_key)
            ht.pop(max_key)
            i+= 1
            
        return res
                
        