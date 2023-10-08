class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        minVal = min(len(word1), len(word2))
        maxVal = max(len(word1), len(word2))
        maxStr = max(word1, word2)
        diff = maxVal - minVal
        
        for i in range(minVal):
            res += word1[i]
            res += word2[i]
                
        if diff > 0:
            if len(word1) > len(word2):
                res += word1[minVal:]
            else:
                res += word2[minVal:]

            
        return res