class Solution:
    def reverseVowels(self, s: str) -> str:
        val = ''
        res = []
        vowels = ['A','E','I','O','U','a','e','i','o','u']

        for l in s:
            res.append(l)
        
        r = len(res) - 1
        i = 0
        
        while r > i:
            if res[i] not in vowels:
                i+= 1
                continue
                
            if res[r] in vowels:
                temp = res[r]
                res[r] = res[i]
                res[i] = temp
                i+= 1
            
            r -= 1
            
        return val.join(res)